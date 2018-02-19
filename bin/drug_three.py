#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 00:37:02 2018
OBJECTIVE: DRUG VECTOR APPLICATION ON three FAULTS
@author: arghanandan
"""

import fns.pathway_drugged as drugpath
import pandas as pd
import fns.combination as cmb
import fns.encoder as en
import matplotlib.pyplot as plt
import time

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
inpv=[0,0,0,0,1]
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
        for k in range(j+1,25):
            cols=cols+[str(i)+","+str(j)+","+str(k)]
output_drugthree=pd.DataFrame(columns=cols)

m=0
while True:
    output_drugthree.loc[m,"Drug Vector"]=' '.join(map(str,drugv))
    l=1
    print("Drug scenario:",drugv,"starts")
    for i in range(1,25):
        for j in range(i+1,25):
            for k in range(j+1,25):
                drugpath.pathway([i,j,k],drugv,inpv,pathv,outv)
                inpv=[0,0,0,0,1]
                output_drugthree.iloc[m,l]=en.encode(outv)
                print("Drug scenario:",m+1,drugv,"  Fault scenario:",l,"   Fault locations:",[i,j,k])
                l=l+1
    print("Drug scenario:",drugv,"ends")
    drugv=cmb.combination(drugv)
    if drugv==False:
        break
    m=m+1
    
#output_drugthree.to_csv("outs/output_drugthree.csv")
      
print("Execution time: ","%0.3f"%(time.clock()-start_time)," seconds")