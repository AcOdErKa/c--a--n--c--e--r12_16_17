#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:51:38 2018

@author: arghanandan
"""

import pandas as pd
import matplotlib.pyplot as plt

df_drugone=pd.read_csv("output_drugone.csv",index_col=0)

plt.figure()
plt.imshow(df_drugone.iloc[:,1:],interpolation=None,cmap=plt.cm.jet)

plt.xticks([i for i in range(25)],df_drugone.columns[1:])
plt.yticks([i for i in range(64)],df_drugone.iloc[:,0])
plt.colorbar()
plt.show()