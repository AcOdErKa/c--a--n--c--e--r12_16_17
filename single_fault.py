#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 21:42:17 2017

@author: arghanandan
"""

import pandas as pd

#Boolean Network introducing fault at ith gate
def pathway(i,inpv,pathv,outv):
    if i==1:
        pathv[0]=1
    else:
        pathv[0]=inpv[0]
    if i==2:
        pathv[1]=1
    else:
        pathv[1]=inpv[0] or inpv[1]
    if i==3:
        pathv[2]=1
    else:
        pathv[2]=inpv[2]
    if i==4:
        pathv[3]=1
    else:
        pathv[3]=inpv[3]
    if i==5:
        pathv[4]=1
    else:
        pathv[4]=pathv[0] or pathv[1] or pathv[2] or pathv[3]
    if i==8:
        pathv[5]=1
    else:
        pathv[5]=pathv[2]
    if i==6:
        pathv[6]=1
    else:
        pathv[6]=pathv[4]
    if i==7:
        inpv[4]=0
    if i==13:
        pathv[7]=1
    else:
        pathv[7]=pathv[6]
    if i==16:
        pathv[8]=1
    else:
        pathv[8]=pathv[6]
    if i==9:
        pathv[9]=1
    else:
        pathv[9]=pathv[6] or pathv[5] or pathv[3]
    if i==14:
        pathv[10]=1
    else:
        pathv[10]=pathv[7]
    if i==17:
        pathv[11]=1
    else:
        pathv[11]=pathv[8]
    if i==10:
        pathv[12]=1
    else:
        pathv[12]=pathv[9] or (int)(not inpv[4])
    if i==15:
        pathv[13]=1
    else:
        pathv[13]=pathv[10]
    if i==18:
        pathv[14]=1
    else:
        pathv[14]=pathv[11]
    if i==11:
        pathv[15]=1
    else:
        pathv[15]=pathv[12]
    if i==12:
        pathv[16]=1
    else:
        pathv[16]=pathv[15]
    if i==20:
        pathv[17]=0
    else:
        pathv[17]=(int)(not pathv[16])
    if i==19:
        pathv[18]=0
    else:
        pathv[18]=(int)(not pathv[16])
    if i==21:
        pathv[19]=1
    else:
        pathv[19]=(int)(not pathv[17])
    if i==22:
        pathv[20]=1
    else:
        pathv[20]=pathv[19]
    if i==23:
        pathv[21]=1
    else:
        pathv[21]=pathv[14] or pathv[15] or pathv[20]
    if i==24:
        pathv[22]=0
    else:
        pathv[22]=(int)(not(pathv[21] or pathv[16]))
    outv[0]=pathv[13] and pathv[21]
    outv[1]=pathv[14]
    outv[2]=pathv[14] and pathv[21]
    outv[3]=pathv[14] and pathv[21]
    outv[4]=(int)(not pathv[22])
    outv[5]=(int)(not pathv[22])
    outv[6]=(int)(not pathv[18])

#reading protein file
df=pd.read_csv("gene.csv",
                delimiter=",",
                index_col=0,
                header=None)

df.columns=["Proteins"]

inp=[]
for i in range(35):
    inp.append(0)
df["Values"]=inp

#pathway and output dataframes
out=pd.DataFrame(df.iloc[28:,:]).reset_index()
path=pd.DataFrame(df.iloc[5:28,:]).reset_index()

#input,pathway and output vectors
inpv=[0,0,0,0,1]
pathv=list(path["Values"])
outv=list(out["Values"])

#output_single_fault dataframe
output_1f=pd.DataFrame(columns=["Output Proteins"])
output_1f["Output Proteins"]=out["Proteins"]

#executing BN at ith gate
for i in range(25):
    pathway(i,inpv,pathv,outv)
    output_1f[str(i)]=outv
    inpv=[0,0,0,0,1]
    
print(output_1f)
