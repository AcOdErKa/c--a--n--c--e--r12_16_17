#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 21:27:00 2018
OBJECTIVE: CALCULATE CONDENSED ENCODED WEIGHTS FOR ALL FAULT SCENARIOS PER DRUG
@author: arghanandan
"""

def condense(converted,convert,case):
    df_con=converted
    df=convert
    if case==1:
        max=88
    elif case==2:
        max=1679.5
    elif case==3:
        max=152655
    col_df=len(df.columns[1:])
    len_df=len(df.index)
    for i in range(len_df):
        weight=0
        for j in range(col_df):
            weight=weight+df.iloc[i,j+1]
        df_con.iloc[i,1]=weight
#    print(df_con)
    df_con.iloc[:,1]=(df_con.iloc[:,1]/max)*100
    return df_con