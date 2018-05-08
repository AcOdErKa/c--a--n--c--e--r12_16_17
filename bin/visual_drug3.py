# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:59:32 2018

@author: akarb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import condenser as cond
plt.style.use("fivethirtyeight")
font="serif"

ifile="outs/output_drugthree.csv"
df_drugone=pd.read_csv(ifile,index_col=0)

col_df=len(df_drugone.columns[1:])
len_df=len(df_drugone.index)

##imageshow: drug vector v fault locations
#plt.figure()
#cax=plt.imshow(df_drugone.iloc[:,1:].T,interpolation="nearest",
#           cmap=plt.cm.RdYlGn_r)
#plt.axis("tight")
#plt.grid(linewidth=0.5)
#plt.xticks([i for i in range(len_df)],df_drugone.iloc[:,0],
#            rotation="vertical",size=8,weight="bold",
#            fontname=font)
#plt.yticks([i for i in range(col_df)],df_drugone.columns[1:],
#            fontname=font,size=3)
#plt.xlabel("DRUG VECTOR",fontname=font)
#plt.ylabel("FAULT LOCATION",fontname=font)
#cbar=plt.colorbar(cax,ticks=np.arange(0.5,9.6,1))
#for l in cbar.ax.yaxis.get_ticklabels():
#    l.set_family(font)
#    l.set_size(10)
#plt.show()

#condensed dataframe to store encoded weights
df_con=cond.condense(df_drugone)
ofile="outs/output_3_weight.csv"
df_con.to_csv(ofile)
df_con=pd.read_csv(ofile,index_col=0)

#scatter: drug vector v encoded weights
plt.figure()
plt.plot([i for i in range(len_df)],df_con.iloc[:,1],".-",c="r",linewidth=1.2)
plt.axis("tight")
plt.xticks([i for i in range(len_df)],df_con.iloc[:,0],
            rotation="vertical",size=8,weight="bold",fontname=font)
plt.yticks(np.arange(0, 100, 5),
           fontname=font,size=10,weight="bold")
plt.xlabel("DRUG VECTOR",fontname=font)
plt.ylabel("CONDENSED WEIGHT",fontname=font)
plt.show()