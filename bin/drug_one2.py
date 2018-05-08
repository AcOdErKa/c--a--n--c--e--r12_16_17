#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 6 12:56:50 2018
OBJECTIVE: DRUG VECTOR APPLICATION ON ONE FAULT USING PARALLELISATION
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

#kernel code for parallel encoding
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
df_gene.columns=["Proteins"]
df_gene["Values"]=[0] * len(df_gene.index)

#pathway and output dataframes
out=pd.DataFrame(df_gene.iloc[28:,:]).reset_index()
path=pd.DataFrame(df_gene.iloc[5:28,:]).reset_index()

#input,pathway and output vectors
f=open("outs/output_unq.txt","r")
unq=f.readline()
unq=list(map(int,unq.split(" ")))
inpv=unq
pathv=list(path["Values"])
outv=list(out["Values"])

#reading drug file
df_drug=pd.read_csv("ins/drug.csv",header=None)
df_drug.columns=["Drugs"]

#creating output and fault file
faultv=[]
cols=["Drug Vector"]
col=[]
for i in range(1,25):
    cols=cols+[str(i)]
    faultv.append([i])
output_drugone=pd.DataFrame(columns=cols)

df_drug=pd.DataFrame(columns=df_drug.iloc[:,0])

#input,pathway and output vectors
f=open("outs/output_unq.txt","r")
unq=f.readline()
unq=list(map(int,unq.split(" ")))
inpv=unq
pathv=[0] * len(path.index)
outv=[[0]*len(out.index)]*len(faultv)

#creating drug file
i=0
drugv=[0,0,0,0,0,0]
while True:
    df_drug.loc[i]=drugv
    drugv=cmb.combination(drugv)
    if drugv==False:
        break
    i=i+1    

#drugv matrix for parallelised input
drugv=(df_drug.as_matrix()).astype(np.int32)

outsize=7
thlen=len(faultv)
kernel=kernel % {"outsize":outsize}
mod=compiler.SourceModule(kernel)
results=mod.get_function("encode")
for i  in range(len(drugv)):
##    print "Drug vector:",i+1,drugv[i],"started."
    for j in range(len(faultv)):
        outlist=[0]*len(out.index)
        drugpath.pathway(faultv[j],drugv[i],inpv,pathv,outlist)
        outv[j]=outlist
        inpv=unq[:]
    outv_gpu=gpuarray.to_gpu((np.array(outv)).astype(np.int32))
    env_gpu=gpuarray.empty((thlen),np.float32)
    results(outv_gpu,env_gpu,block=(thlen,1,1))
    output_drugone.loc[i]=" ".join(map(str,drugv[i]))
    output_drugone.iloc[i,1:]=env_gpu.get()
##    print "Drug vector:",i+1,drugv[i],"end."

ofile="outs/output_drugone_p.csv"
output_drugone.to_csv(ofile)
print "Output written to",ofile
      
print "Execution time: ","%0.3f"%(time.clock()-start_time),"seconds"
