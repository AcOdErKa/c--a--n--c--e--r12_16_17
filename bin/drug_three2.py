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
df_gene.columns=["Proteins"]
df_gene["Values"]=[0] * len(df_gene.index)

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

#input,pathway and output vectors
inpv=[0,0,0,0,1]
pathv=[0]*len(path)
outv=[[0]*len(out)]* len(faultv)

#reading drug file
df_drug=pd.read_csv("ins/drug.csv",header=None)
df_drug.columns=["Drugs"]
df_drug["Values"]=[0] * len(df_drug.index)
