#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 16:24:38 2018

@author: arghanandan
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.style.use("fivethirtyeight")
font="serif"

df=pd.read_csv("ins_time/drug_time.csv")

plt.figure()
cpu_time=df.iloc[0,1:5].as_matrix()
gpu_time=df.iloc[0,5:].as_matrix()
plt.plot([i+1 for i in range(4)],cpu_time,"o--",
          label="CPU",linewidth=1.2,c=(.5,0.5,0,1))
plt.plot([i+1 for i in range(4)],gpu_time,"o-",
          label="GPU",linewidth=1.2,c=(0,0.5,0,1))
plt.xticks([i for i in range(1,5)],[i for i in range(1,5)],
            size=10,weight="bold",fontname=font)
plt.yticks(np.arange(0,2000,100),size=10,weight="bold",fontname=font)
plt.xlabel("CONCURRENT FAULT SCENARIO",fontname=font)
plt.ylabel("EXECUTION TIME (s)",fontname=font)
plt.ylim(-100,2000)
cl=plt.legend(title="Execution time",loc=2)
plt.setp(cl.texts,family=font,size=12)
plt.setp(cl.get_title(),family=font,size=10)
plt.show()