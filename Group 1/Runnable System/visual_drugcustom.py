#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:10:15 2018

@author: arghanandan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import condenser as cond
plt.style.use("bmh")

ifile="outs/output_custom1.csv"
df_drugone=pd.read_csv(ifile,index_col=0)

col_df=len(df_drugone.columns[1:])
len_df=len(df_drugone.index)

#imageshow: drug vector v fault locations
#plt.figure()
#plt.title("DRUG VECTORS V FAULT LOCATIONS\n" + ifile)
#plt.imshow(df_drugone.iloc[:,1:],interpolation="sinc",cmap=plt.cm.RdYlGn_r)
#plt.axis("tight")
#plt.xticks([i for i in range(col_df)],df_drugone.columns[1:])
#plt.xlabel("Fault Location")
#plt.yticks([i for i in range(len_df)],df_drugone.iloc[:,0])
#plt.ylabel("Drug Vector")
#plt.colorbar()
#plt.show()

#condensed dataframe to store encoded weights
df_con=cond.condense(df_drugone)
ofile="outs/output_custom_weight.csv"
df_con.to_csv(ofile)
df_con=pd.read_csv(ofile,index_col=0)

#scatter: drug vector v encoded weights
plt.figure()
plt.title("DRUG VECTORS V CONDENSED WEIGHTS\n" + ofile)
plt.plot([i for i in range(len_df)],df_con.iloc[:,1])
plt.axis("tight")
plt.xticks([i for i in range(len_df)],df_con.iloc[:,0],rotation="vertical")
plt.yticks(np.arange(min(df_con.iloc[:,1]), max(df_con.iloc[:,1])+5, 5))
plt.xlabel("Drug Vector")
plt.ylabel("Condensed Weight")
plt.legend()
plt.show()