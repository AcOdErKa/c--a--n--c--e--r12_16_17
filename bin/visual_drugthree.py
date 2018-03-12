# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:59:32 2018

@author: akarb
"""

import pandas as pd
import numpy as np
import condenser as cond
import matplotlib.pyplot as plt
plt.style.use("bmh")

ifile="outs/output_drugthree_p.csv"
df_drugthree=pd.read_csv(ifile,index_col=0)

col_df=len(df_drugthree.columns[1:])
len_df=len(df_drugthree.index)

#plt.figure()
#plt.imshow(df_drugthree.iloc[:,1:],interpolation="sinc",cmap=plt.cm.RdYlGn_r)
#plt.axis("tight")
#plt.title(ifile)
#plt.xticks([i for i in range(col_df)],df_drugthree.columns[1:],rotation="vertical")
#plt.yticks([i for i in range(len_df)],df_drugthree.iloc[:,0])
#plt.xlabel("fault locations")
#plt.ylabel("drug vector")
#plt.colorbar()
#plt.show()

df_con=pd.DataFrame(columns=["Drug Vector","Encoded weightage"])
df_con.iloc[:,0]=df_drugthree.iloc[:,0]
df_con=cond.condense(df_con,df_drugthree,3)

ofile="outs/output_drugthree_weight.csv"
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