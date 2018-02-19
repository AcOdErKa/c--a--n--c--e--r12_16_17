#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:44:50 2018

@author: arghanandan
"""
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("bmh")

ifile="outs/output_drugtwo2.csv"
df_drugtwo=pd.read_csv(ifile,index_col=0)

plt.figure()
plt.imshow(df_drugtwo.iloc[:,1:],interpolation="sinc",cmap=plt.cm.RdYlGn_r)
plt.axis("tight")
plt.title(ifile)
plt.xticks([i for i in range(276)],df_drugtwo.columns[1:])
plt.yticks([i for i in range(64)],df_drugtwo.iloc[:,0])
plt.colorbar()
plt.show()

df_con=pd.DataFrame(columns=["Drug Vector","Encoded weightage"])
df_con.iloc[:,0]=df_drugtwo.iloc[:,0]

for i in range(len(df_drugtwo.index)):
    weight=0
    for j in range(276):
        weight=weight+df_drugtwo.iloc[i,j+1]
    df_con.iloc[i,1]=weight
    
df_con.iloc[:,1]=df_con.iloc[:,1]/(df_con.iloc[:,1].max()/2)
ofile="outs/output_drugtwo_weight2.csv"
df_con.to_csv(ofile)
df_con=pd.read_csv(ofile,index_col=0)
   
plt.figure()
plt.imshow(df_con.iloc[:,1:],interpolation="nearest",cmap=plt.cm.RdYlGn_r)
plt.axis("tight")
plt.title(ofile)
plt.xticks([],[])
plt.yticks([i for i in range(64)],df_con.iloc[:,0])
plt.colorbar()
plt.show()
