#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 6 14:02:09 2018
DRUG VECTOR APPLICATION ON FOUR FAULTS USING PARALLELISATION
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
__global__ void encode(int *outv,float *env)
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
    env[tx]=(0.5*(f*s)) + (0.5*(f+s));
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
nodes=25
for i in range(1,nodes):
    for j in range(i+1,nodes):
        for k in range(j+1,nodes):
            for l in range(k+1,nodes):
                cols=cols+[str(i)+","+str(j)+","+str(k)+","+str(l)]
                faultv.append([i,j,k,l])
output_drugthree=pd.DataFrame(columns=cols)
df_drug=pd.DataFrame(columns=df_drug.iloc[:,0])

#input,pathway and output vectors
f=open("outs/output_unq.txt","r")
unq=f.readline()
unq=list(map(int,unq.split(" ")))
inpv=unq
pathv=[0]*len(path)
outv=[[0]*len(out)]* len(faultv)
env=[0] * len(faultv)

#creating drugv file
i=0
drugv=[0]*len(df_drug.columns)
while True:
    df_drug.loc[i]=drugv
    drugv=cmb.combination(drugv)
    if drugv==False:
        break
    i=i+1
drugv=(df_drug.as_matrix()).astype(np.int32)

outsize=7
thsize=1024
faultsize=len(faultv)
kernel=kernel % {"outsize":outsize}
mod=compiler.SourceModule(kernel)
results=mod.get_function("encode")
for i in range(len(drugv)):
##    print "Drug vector:",i+1,list(drugv[i]),"started."
    for j in range(faultsize):
        outlist=[0]*outsize
        drugpath.pathway(faultv[j],drugv[i],inpv,pathv,outlist)
        outv[j]=outlist
        inpv=unq[:]
    output_drugthree.loc[i]=" ".join(map(str,drugv[i]))
    thlen=0
    while (thlen+thsize)<faultsize:
        outv_gpu=gpuarray.to_gpu((np.array(outv[thlen:thlen+thsize])).astype(np.int32))
        env_gpu=gpuarray.empty(thsize,np.float32)
        results(outv_gpu,env_gpu,block=(thsize,1,1))
        output_drugthree.iloc[i,thlen+1:thlen+thsize+1]=env_gpu.get()
        thlen=thlen+thsize
    left=faultsize-thlen
    if left>0:
        outv_gpu=gpuarray.to_gpu((np.array(outv[thlen:])).astype(np.int32))
        env_gpu=gpuarray.empty(left,np.float32)
        results(outv_gpu,env_gpu,block=(left,1,1))
        output_drugthree.iloc[i,thlen+1:]=env_gpu.get()
##    print "Drug vector:",i+1,list(drugv[i]),"ended."

ofile="outs/output_drugthree_p.csv"
output_drugthree.to_csv(ofile)
print "Output written to",ofile

print "Execution time: ","%0.3f"%(time.clock()-start_time)," seconds"
