#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:44:50 2018

@author: arghanandan
"""
import pandas as pd
import matplotlib.pyplot as plt

df_drugtwo=pd.read_csv("output_drugtwo.csv",index_col=0)

plt.figure()
plt.imshow(df_drugtwo.iloc[:,1:],interpolation=None,cmap=plt.cm.jet)
plt.xticks([i for i in range(276)],df_drugtwo.columns[1:])
plt.yticks([i for i in range(64)],df_drugtwo.iloc[:,0])
plt.colorbar()
plt.show()
