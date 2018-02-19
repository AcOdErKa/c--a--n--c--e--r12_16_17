#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:51:38 2018

@author: arghanandan
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("bmh")

df_drugone=pd.read_csv("outs/output_drugone.csv",index_col=0)
#
#plt.figure()
#plt.title("DRUG VECTORS V FAULT LOCATIONS")
#plt.imshow(df_drugone.iloc[:,1:],interpolation="sinc",cmap=plt.cm.RdYlGn_r)
#plt.axis("tight")
#plt.xticks([i for i in range(25)],df_drugone.columns[1:])
#plt.xlabel("Fault Location")
#plt.yticks([i for i in range(64)],df_drugone.iloc[:,0])
#plt.ylabel("Drug Vector")
#plt.colorbar()
#plt.show()

df_con=pd.DataFrame(columns=["Drug Vector","Encoded Weightage"])
df_con.iloc[:,0]=df_drugone.iloc[:,0]

for i in range(len(df_drugone.index)):
    weight=0
    for j in range(25):
        weight=weight+df_drugone.iloc[i,j+1]
    df_con.iloc[i,1]=weight
  
df_con.iloc[:,1]=df_con.iloc[:,1]/(df_con.iloc[:,1].max()/2)
df_con.to_csv("outs/output_drugone_weight.csv")
df_con=pd.read_csv("outs/output_drugone_weight.csv",index_col=0)
   
#plt.figure()
#plt.title("DRUG VECTORS V ENCODED WEIGHTS")
#plt.imshow(df_con.iloc[:,1:],interpolation="nearest",cmap=plt.cm.RdYlGn_r)
#plt.axis("tight")
#plt.xticks([],[])
#plt.xlabel("Encoded Weight")
#plt.yticks([i for i in range(64)],df_con.iloc[:,0])
#plt.ylabel("Drug Vector")
#plt.colorbar()
#plt.show()

df_same=pd.DataFrame(columns=df_con.columns)

j=0
for i in range(64):
    if df_con.iloc[i,1].item()==df_con.iloc[:,1].min():
        df_same.loc[j]=df_con.loc[i]
        j=j+1

#print(df_same)
plt.figure()
plt.title("DRUG VECTORS V ENCODED WEIGHTS")
plt.scatter(df_con.iloc[:,0],df_con.iloc[:,1])#df_same["Encoded Weightage"],df_same["Drug Vector"])
plt.axis("tight")
#plt.xticks([],[])
plt.xlabel("Drug Vector")
plt.xticks([i for i in range(64)],df_con.iloc[:,0],rotation="vertical")
plt.ylabel("Encoded Weight")
plt.legend()
plt.show()