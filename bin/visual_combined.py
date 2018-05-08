#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:01:40 2018

@author: arghanandan
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.style.use("fivethirtyeight")
colors=['r','b','g','black']
font="serif"

k=0
plt.figure()
plt.xlabel("DRUG VECTOR",fontname=font)
plt.ylabel("CONDENSED WEIGHT",fontname=font)

for i in range(3):
    cols=["drug vector",str(i+1)+" faults"]
    df=pd.read_csv("outs/output_"+str(i+1)+"_weight.csv",index_col=0)
    df.columns=cols
    df_sel=pd.DataFrame(columns=cols)
    for j in range(len(df.index)):
        drugv=df.iloc[j,0].split(" ")
        if drugv[3]=='1':
            df_sel.loc[k]=df.loc[j]
            k+=1
    plt.plot(df_sel.iloc[:,0],df_sel.iloc[:,1],'.-',c=colors[i],linewidth=1.2)
    plt.axis("tight")
    plt.xticks([i for i in range(len(df_sel.index))],df_sel.iloc[:,0],
            rotation="vertical",size=9,weight="bold",fontname=font)
    plt.yticks(np.arange(30, 101, 5),
           fontname=font,size=10,weight="bold")
    plt.show()

cl=plt.legend(loc=2)
plt.setp(cl.texts,family=font)