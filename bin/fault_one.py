#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:42:17 2017
INDUCING SINGLE FAULTS IN BOOLEAN NETWORK
@author: arghanandan
"""
import pandas as pd
import pathway_normal as pth
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)

#reading protein file
df=pd.read_csv("gene.csv",
                delimiter=",",
                index_col=0,
                header=None)

df.columns=["Proteins"]
df["Values"]=[0] * len(df.index)

#pathway and output dataframes
out=pd.DataFrame(df.iloc[28:,:]).reset_index()
path=pd.DataFrame(df.iloc[5:28,:]).reset_index()

#input,pathway and output vectors
inpv=[0,0,0,0,1]
pathv=list(path["Values"])
outv=list(out["Values"])

#output_single_fault dataframe
output_1f=pd.DataFrame(columns=["Output Proteins"])
output_1f["Output Proteins"]=out["Proteins"]

#executing BN at ith gate
for i in range(25):
    pth.pathway([i],inpv,pathv,outv)
    output_1f[str(i)]=outv
    inpv=[0,0,0,0,1]
    
print(output_1f)

#write to .csv file   
#output_1f.to_csv("output_1f.csv")