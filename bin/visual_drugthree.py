# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:59:32 2018

@author: akarb
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("bmh")

ifile="outs/output_drugthree_p.csv"
df_drugthree=pd.read_csv(ifile,index_col=0)

col_df=len(df_drugthree.columns[1:])
len_df=len(df_drugthree.index)

plt.figure()
plt.imshow(df_drugthree.iloc[:,1:],interpolation="sinc",cmap=plt.cm.RdYlGn_r)
plt.axis("tight")
plt.title(ifile)
plt.xticks([i for i in range(col_df)],df_drugthree.columns[1:],rotation="vertical")
plt.yticks([i for i in range(len_df)],df_drugthree.iloc[:,0])
plt.xlabel("fault locations")
plt.ylabel("drug vector")
plt.colorbar()
plt.show()

df_con=pd.DataFrame(columns=["Drug Vector","Encoded weightage"])
df_con.iloc[:,0]=df_drugthree.iloc[:,0]

for i in range(len(df_drugthree.index)):
    weight=0
    for j in range(col_df):
        weight=weight+df_drugthree.iloc[i,j+1]
    df_con.iloc[i,1]=weight
    
df_con.iloc[:,1]=df_con.iloc[:,1]/(df_con.iloc[:,1].max()/2)
ofile="outs/output_drugthree_weight.csv"
df_con.to_csv(ofile)
df_con=pd.read_csv(ofile,index_col=0)
   
plt.figure()
plt.imshow(df_con.iloc[:,1:],interpolation="nearest",cmap=plt.cm.RdYlGn_r)
plt.axis("tight")
plt.title(ofile)
plt.xticks([],[])
plt.yticks([i for i in range(len_df)],df_con.iloc[:,0])
plt.xlabel("encoded weight")
plt.ylabel("drug vector")
plt.colorbar()
plt.show()
