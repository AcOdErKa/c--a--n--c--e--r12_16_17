#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:55:56 2017
CHECKING INPUT VECTORS ON SIGNALLING PATHWAY
@author: arghanandan
"""

#for DataFrames
import pandas as pd
import matplotlib.pyplot as plt

#calculating output of signalling pathway
def pathway(inpv,pathv,outv):
    pathv[0]=inpv[0]
    pathv[1]=inpv[0] or inpv[1]
    pathv[2]=inpv[2]
    pathv[3]=inpv[3]
    pathv[4]=pathv[0] or pathv[1] or pathv[2] or pathv[3]
    pathv[5]=pathv[2]
    pathv[6]=pathv[4]
    pathv[7]=pathv[6]
    pathv[8]=pathv[6]
    pathv[9]=pathv[6] or pathv[5] or pathv[3]
    pathv[10]=pathv[7]
    pathv[11]=pathv[8]
    pathv[12]=pathv[9] or (int)(not inpv[4])
    pathv[13]=pathv[10]
    pathv[14]=pathv[11]
    pathv[15]=pathv[12]
    pathv[16]=pathv[15]
    pathv[17]=(int)(not pathv[16])
    pathv[18]=(int)(not pathv[16])
    pathv[19]=(int)(not pathv[17])
    pathv[20]=pathv[19]
    pathv[21]=pathv[14] or pathv[15] or pathv[20]
    pathv[22]=(int)(not(pathv[21] or pathv[16]))
    outv[0]=pathv[13] and pathv[21]
    outv[1]=pathv[14]
    outv[2]=pathv[14] and pathv[21]
    outv[3]=pathv[14] and pathv[21]
    outv[4]=(int)(not pathv[22])
    outv[5]=(int)(not pathv[22])
    outv[6]=(int)(not pathv[18])
    
#combination of input vector
def combination(inp):
    i=4
    while inp[i]==1:
        inp[i]=0
        i=i-1
    if i==-1:
        return False
    inp[i]=1
    return inp

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

#input,pathway and output dataframes
out=pd.DataFrame(df.iloc[28:,:]).reset_index()
inp=pd.DataFrame(df.iloc[:5,:])
path=pd.DataFrame(df.iloc[5:28,:]).reset_index()

#input,pathway and output vectors
inpv=list(inp["Values"])
pathv=list(path["Values"])
outv=list(out["Values"])

#output_faultless dataframe
cols=["Input"] + list(out["Proteins"])
output_fl=pd.DataFrame(columns=cols)

#pathway_faultless dataframe
path_fl=pd.DataFrame(columns=["Proteins","Values"])
path_fl.Proteins=path["Proteins"]

#output vector for each input combination
for i in range(32):
    pathway(inpv,pathv,outv)
    output_fl.loc[i,"Input"]=' '.join(map(str,inpv))
    if i==0:
        path_fl["Values"]=pathv
    output_fl.iloc[i,1:]=outv
    inpv=combination(inpv)
    if inpv==False:
        break
    
for i in range(32):
    out=list(output_fl.iloc[i,1:])
    if out==[0,0,0,0,0,0,0]:
        unq=out
        break

print("1. Check Network\n2. Fault-less DataFrame\n3. Unique Input Vector")
n=int(input("Enter choice: "))

if n==1:
    print("Input vector: [0,0,0,0,0]\n")
    print(path_fl)
elif n==2:
    print(output_fl)
elif n==3:
    print("Unique input vector: " + str(unq))

#plotting input vectors       
#plt.figure()
#for i in range(5):
#    plt.xticks(range(7),output_fl.columns[1:])
#    plt.yticks(range(2),[0,1])
#    plt.plot(range(7),output_fl.iloc[i,1:],alpha=0.3,label=output_fl.loc[i,'Input'])
#plt.legend()
#plt.show()
#
#write to .csv file   
#output_fl.to_csv("output_fl.csv")