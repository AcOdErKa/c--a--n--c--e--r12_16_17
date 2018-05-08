#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:07:50 2018
OBJECTIVE: DRUG VECTOR APPLICATION ON TWO FAULTS
@author: arghanandan
"""

import pathway_drugged as drugpath
import pandas as pd
import combination as cmb
import encoder as en
import matplotlib.pyplot as plt
import time

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
unq=unq.split(" ")
inpv=list(map(int,unq))
pathv=list(path["Values"])
outv=list(out["Values"])

#reading drug file
df_drug=pd.read_csv("ins/drug.csv",header=None)
df_drug.columns=["Drugs"]
df_drug["Values"]=[0] * len(df_drug.index)

drugv=list(df_drug["Values"])

#creating output file
cols=["Drug Vector"]
for i in range(1,25):
    for j in range(i+1,25):
        cols=cols+[str(i)+","+str(j)]
output_drugtwo=pd.DataFrame(columns=cols)

k=0
start_time=time.clock()
while True:
    output_drugtwo.loc[k,"Drug Vector"]=' '.join(map(str,drugv))
    l=1
    for i in range(1,25):
        for j in range(i+1,25):
            drugpath.pathway([i,j],drugv,inpv,pathv,outv)
            inpv=[0,0,0,0,1]
            output_drugtwo.iloc[k,l]=en.encode(outv)
            l=l+1
    drugv=cmb.combination(drugv)
    if drugv==False:
        break
    k=k+1

print("Execution time: ","%0.3f"%(time.clock()-start_time)," seconds")    

output_drugtwo.to_csv("outs/output_drugtwo.csv")