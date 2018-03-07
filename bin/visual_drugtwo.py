#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:44:50 2018

@author: arghanandan
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("bmh")

ifile="outs/output_drugtwo.csv"
df_drugtwo=pd.read_csv(ifile,index_col=0)

col_df=len(df_drugtwo.columns[1:])
len_df=len(df_drugtwo.index)

#plt.figure()
#plt.imshow(df_drugtwo.iloc[:,1:],interpolation="sinc",cmap=plt.cm.RdYlGn_r)
#plt.axis("tight")
#plt.title("DRUG VECTORS V FAULT LOCATIONS")
#plt.suptitle(ifile)
#plt.xticks([i for i in range(col_df)],df_drugtwo.columns[1:],rotation="vertical")
#plt.yticks([i for i in range(len_df)],df_drugtwo.iloc[:,0])
#plt.xlabel("Fault Locations")
#plt.ylabel("Drug vector")
#plt.colorbar()
#plt.show()

df_con=pd.DataFrame(columns=["Drug Vector","Encoded weightage"])
df_con.iloc[:,0]=df_drugtwo.iloc[:,0]

for i in range(len(df_drugtwo.index)):
    weight=0
    for j in range(col_df):
        weight=weight+df_drugtwo.iloc[i,j+1]
    df_con.iloc[i,1]=weight
    
df_con.iloc[:,1]=df_con.iloc[:,1]/(df_con.iloc[:,1].max()/2)
ofile="outs/output_drugtwo_weight.csv"
df_con.to_csv(ofile)
df_con=pd.read_csv(ofile,index_col=0)
   
#plt.figure()
#plt.imshow(df_con.iloc[:,1:],interpolation="nearest",cmap=plt.cm.RdYlGn_r)
#plt.axis("tight")
#plt.title("DRUG VECTORS V ENCODED WEIGHTS")
#plt.suptitle(ofile)
#plt.yticks([i for i in range(len_df)],df_con.iloc[:,0])
#plt.xlabel("Encoded Weights")
#plt.ylabel("Drug Vector")
#plt.colorbar()
#plt.show()
