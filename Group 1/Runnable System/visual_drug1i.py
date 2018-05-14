#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 00:17:34 2018

@author: arghanandan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
font="serif"

ifile="outs/output_drugone.csv"
df_drugone=pd.read_csv(ifile,index_col=0)

col_df=len(df_drugone.columns[1:])
len_df=len(df_drugone.index)

#imageshow: drug vector v fault locations
plt.figure()
cax=plt.imshow(df_drugone.iloc[:,1:].T,interpolation="nearest",
           cmap=plt.cm.RdYlGn_r)
plt.axis("tight")
plt.grid(linewidth=0.5)
plt.xticks([i for i in range(len_df)],df_drugone.iloc[:,0],
            rotation="vertical",size=8,weight="bold",
            fontname=font)
plt.yticks([i for i in range(col_df)],df_drugone.columns[1:],
            fontname=font,size=10,weight="bold")
plt.xlabel("DRUG VECTOR",fontname=font)
plt.ylabel("FAULT LOCATION",fontname=font)
plt.title("DRUG VECTORS v SINGLE FAULT LOCATIONS")
cbar=plt.colorbar(cax,ticks=np.arange(0.5,9.6,1))
for l in cbar.ax.yaxis.get_ticklabels():
    l.set_family(font)
    l.set_size(10)
plt.show()
