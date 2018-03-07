#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:40:02 2018
OBJECTIVE: DRUG VECTOR APPLICATION ON THREE FAULTS USING PARALLELISATION
@author: arghanandan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import combination as cmb
import pathway_drugged as drugpath
import numpy as np
from pycuda import driver, compiler, gpuarray, tools
import pycuda.autoinit

kernel="""
__global__ void encode(int *outv,int *env)
{
    int tx=threadIdx.x;
    
    int p=tx*(%(outsize)s);
    int f=0,s=0;
    
    for(int i=0;i<%(outsize)s;i++)
    {
        if(i<4)
            f+=outv[p+i];
        else
            s+=outv[p+i];
    }
    env[tx]=(5*(f*s)) + (5*(f+s));
}
"""
start_time=time.clock()

#common settings
plt.style.use("ggplot")
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
        
#reading protein file
df_gene=pd.read_csv("ins/gene.csv",
                delimiter=",",
                index_col=0,
                header=None)
df_gene.columns=["proteins"]
df_gene["values"]=[0] * len(df_gene.index)

#reading drug file
df_drug=pd.read_csv("ins/drug.csv",header=None)
df_drug.columns=["Drugs"]

#pathway and output dataframes
out=pd.DataFrame(df_gene.iloc[28:,:]).reset_index()
path=pd.DataFrame(df_gene.iloc[5:28,:]).reset_index()

#creating output and fault file
faultv=[]
cols=["drug vector"]
for i in range(1,25):
    for j in range(i+1,25):
        for k in range(j+1,25):
            cols=cols+[str(i)+","+str(j)+","+str(k)]
            faultv.append([i,j,k])
output_drugthree=pd.DataFrame(columns=cols)
df_drug=pd.DataFrame(columns=df_drug.iloc[:,0])

#input,pathway and output vectors
f=open("outs/output_unq.txt","r")
unq=f.readline()
unq=unq.split(" ")
inpv=list(map(int,unq))
pathv=[0]*len(path)
outv=[[0]*len(out)]* len(faultv)
env=[0] * len(faultv)

#creating drugv file
i=0
drugv=[0,0,0,0,0,0]
while True:
    df_drug.loc[i]=drugv
    drugv=cmb.combination(drugv)
    if drugv==False:
        break
    i=i+1
drugv=(df_drug.as_matrix()).astype(np.int32)

outsize=7
thlen=len(faultv)/2
kernel=kernel % {"outsize":outsize}
mod=compiler.SourceModule(kernel)
results=mod.get_function("encode")
for i in range(len(drugv)):
    print "Drug vector:",i+1,list(drugv[i]),"started."
    for j in range(len(faultv)):
        outlist=[0,0,0,0,0,0,0]
        drugpath.pathway(faultv[j],drugv[i],inpv,pathv,outlist)
        outv[j]=outlist
        inpv=[0,0,0,0,1]
    output_drugthree.loc[i]=" ".join(map(str,drugv[i]))
    outv_gpu=gpuarray.to_gpu((np.array(outv[:thlen])).astype(np.int32))
    env_gpu=gpuarray.empty(thlen,np.int32)
    results(outv_gpu,env_gpu,block=(thlen,1,1))
    output_drugthree.iloc[i,1:thlen+1]=env_gpu.get()
    outv_gpu=gpuarray.to_gpu((np.array(outv[thlen:])).astype(np.int32))
    env_gpu=gpuarray.empty(thlen,np.int32)
    results(outv_gpu,env_gpu,block=(thlen,1,1))
    output_drugthree.iloc[i,thlen+1:]=env_gpu.get()
    print "Drug vector:",i+1,list(drugv[i]),"ended."

ofile="outs/output_drugthree_p.csv"
output_drugthree.to_csv(ofile)
print "Output written to",ofile

print "Execution time: ","%0.3f"%(time.clock()-start_time)," seconds"
