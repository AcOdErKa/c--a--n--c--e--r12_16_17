#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 10:44:30 2018
OBJECTIVE: INDUCE TWO FAULTS IN BOOLEAN NETWORK
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

inp=[]
for i in range(35):
    inp.append(0)
df["Values"]=inp

#pathway and output dataframes
out=pd.DataFrame(df.iloc[28:,:]).reset_index()
path=pd.DataFrame(df.iloc[5:28,:]).reset_index()

#input,pathway and output vectors
inpv=[0,0,0,0,1]
pathv=list(path["Values"])
outv=list(out["Values"])

#output_single_fault dataframe
output_2f=pd.DataFrame(columns=["Output Proteins"])
output_2f["Output Proteins"]=out["Proteins"]

#executing BN at ith gate
for i in range(1,25):
    for j in range(i,25):
        if i!=j:
            pth.pathway([i,j],inpv,pathv,outv)
            output_2f[str(i)+","+str(j)]=outv
            inpv=[0,0,0,0,1]
            
print(output_2f)

#write to .csv file   
#output_2f.to_csv("output_2f.csv")