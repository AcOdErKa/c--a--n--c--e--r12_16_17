#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:11:14 2018
OBJECTIVE: DRUG VECTOR APPLICATION ON SINGLE FAULT
@author: arghanandan
"""

import pathway_drugged as drugpath
import pandas as pd
import combination as cmb
import encoder as en
import matplotlib.pyplot as plt
import time

start_time=time.clock()

#common settings
plt.style.use("ggplot")
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
        
#reading protein file
df_gene=pd.read_csv("gene.csv",
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
df_drug=pd.read_csv("drug.csv",header=None)
df_drug.columns=["Drugs"]
df_drug["Values"]=[0] * len(df_drug.index)

drugv=list(df_drug["Values"])

#creating output file
cols=["Drug Vector"] + [i for i in range(25)]
output_drugone=pd.DataFrame(columns=cols)

j=0
while True:
    encoded=[]
    for i in range(25):
        drugpath.pathway([i],drugv,inpv,pathv,outv)
        encoded.append(float(en.encode(outv)))
        inpv=[0,0,0,0,1]
    output_drugone.loc[j,"Drug Vector"]=' '.join(map(str,drugv))
    output_drugone.iloc[j,1:]=encoded
    drugv=cmb.combination(drugv)
    if drugv==False:
        break
    j=j+1

for i in range(24):
    pd.to_numeric(output_drugone[i+1])

#print(output_drugone)

#plt.figure()
#plt.imshow(output_drugone.iloc[:,1:],interpolation='bicubic',cmap='hot')
#plt.colorbar()
#plt.xticks(25,[i for i in range(24)])
#plt.yticks(64,output_drugone.iloc[:,0])
#plt.show()

#write to output_drugone.csv
#output_drugone.to_csv("output_drugone.csv")
    
print("Execution time: ","%0.3f"%(time.clock()-start_time)," seconds")