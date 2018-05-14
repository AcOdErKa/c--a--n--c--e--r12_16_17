#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:55:56 2017
CHECKING INPUT VECTORS ON SIGNALLING PATHWAY
@author: arghanandan
"""

#for DataFrames
import pandas as pd
import pathway_normal as pth
import combination as cmb

#reading protein file
df=pd.read_csv("ins/gene.csv",
                delimiter=",",
                index_col=0,
                header=None)

df.columns=["Proteins"]

inp=[]
for i in range(35):
    inp.append(0)
df["Values"]=inp

#input,pathway and output dataframes
out=pd.DataFrame(df.iloc[28:,:]).reset_index()
inp=pd.DataFrame(df.iloc[:5,:])
path=pd.DataFrame(df.iloc[5:28,:]).reset_index()

#input,pathway and output vectors
inpv=list(inp["Values"])
pathv=list(path["Values"])
outv=list(out["Values"])

#output_faultless dataframe
cols=["Input"] + list(out["Proteins"])
output_fl=pd.DataFrame(columns=cols)

#pathway_faultless dataframe
path_fl=pd.DataFrame(columns=["Proteins","Values"])
path_fl.Proteins=path["Proteins"]

#output vector for each input combination
for i in range(32):
    pth.pathway([0],inpv,pathv,outv)
    output_fl.loc[i,"Input"]=' '.join(map(str,inpv))
    if i==0:
        path_fl["Values"]=pathv
    if outv==[0,0,0,0,0,0,0]:
        unq=list(map(int,(output_fl.loc[i,"Input"]).split(" ")))
    output_fl.iloc[i,1:]=outv
    inpv=cmb.combination(inpv)
    if inpv==False:
        break
    
#write to .csv file   
output_fl.to_csv("outs/output_fl.csv")
print(output_fl)
print "rows: ",len(output_fl.index),"\tcolumns: ",len(output_fl.columns)
print "Unique input vector: ",unq

#write unique_input_vector to file
f=open("outs/output_unq.txt","w")
f.write(" ".join(map(str,unq)))
f.close()
