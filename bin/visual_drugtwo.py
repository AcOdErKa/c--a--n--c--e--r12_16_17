#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:44:50 2018

@author: arghanandan
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import condenser as cond
plt.style.use("bmh")

ifile="outs/output_drugtwo.csv"
df_drugtwo=pd.read_csv(ifile,index_col=0)

col_df=len(df_drugtwo.columns[1:])
len_df=len(df_drugtwo.index)

plt.figure()
plt.imshow(df_drugtwo.iloc[:,1:],interpolation="sinc",cmap=plt.cm.RdYlGn_r)
plt.axis("tight")
plt.title("DRUG VECTORS V FAULT LOCATIONS\n" + ifile)
plt.xticks([i for i in range(col_df)],df_drugtwo.columns[1:],rotation="vertical")
plt.yticks([i for i in range(len_df)],df_drugtwo.iloc[:,0])
plt.xlabel("Fault Locations")
plt.ylabel("Drug vector")
plt.colorbar()
plt.show()

df_con=pd.DataFrame(columns=["Drug Vector","Encoded weightage"])
df_con.iloc[:,0]=df_drugtwo.iloc[:,0]
df_con=cond.condense(df_con,df_drugtwo,2)

ofile="outs/output_drugtwo_weight.csv"
df_con.to_csv(ofile)
df_con=pd.read_csv(ofile,index_col=0)
   
#scatter: drug vector v encoded weights
plt.figure()
plt.title("DRUG VECTORS V CONDENSED WEIGHTS\n" + ofile)
plt.scatter([i for i in range(len_df)],df_con.iloc[:,1])
plt.axis("tight")
plt.xticks([i for i in range(len_df)],df_con.iloc[:,0],rotation="vertical")
plt.yticks(np.arange(0, 105, 5))
plt.xlabel("Drug Vector")
plt.ylabel("Condensed Weight")
plt.legend()
plt.show()