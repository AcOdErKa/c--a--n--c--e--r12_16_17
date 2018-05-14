#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:40:34 2018
OBJECTIVE: TEST NEW LOCATIONS IN THE NETWORK FOR BETTER DRUG INPUTS
@author: arghanandan
"""

import pandas as pd
import pathway_custom as drugpath
import encoder as en
import time

start_time=time.clock()

#common settings
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
        
#reading protein file
df_gene=pd.read_csv("ins/gene.csv",
                delimiter=",",
                index_col=0,
                header=None)
df_gene.columns=["proteins"]
df_gene["values"]=[0] * len(df_gene.index)

#pathway and output dataframes
out=pd.DataFrame(df_gene.iloc[28:,:]).reset_index()
path=pd.DataFrame(df_gene.iloc[5:28,:]).reset_index()

#input,pathway and output vectors
f=open("outs/output_unq.txt","r")
unq=f.readline()
unq=unq.split(" ")
inpv=list(map(int,unq))
pathv=list(path["values"])
outv=list(out["values"])

#creating custom drug file
df_drug=pd.DataFrame()
df_drug["drug"]=["DRG"+str(i+1) for i in range(24)]

#drugv and encoded lists
k=0
drugv=["" for i in range(276)]
for i in range(24):
    for j in range(i+1,24):
        drugv[k]=[df_drug.iloc[i,0],df_drug.iloc[j,0]]
        k=k+1
encoded=[0 for i in range(25)]

#output dataframe
output_custom=pd.DataFrame(columns=["drug"]+[str(i) for i in range(25)])

j=0
while True:
    for i in range(25):
        drugpath.pathway([i],drugv[j],inpv,pathv,outv)
        encoded[i]=en.encode(outv)
    output_custom.loc[j]=[drugv[j][0]+","+drugv[j][1]]+encoded
    inpv=[0,0,0,0,1]
    j=j+1
    if j==len(drugv):
        break
#print(output_custom)

#write to csv
output_custom.to_csv("outs/output_custom1.csv")