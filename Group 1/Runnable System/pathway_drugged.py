#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:10:13 2018
OBJECTIVE: NETWORK PATHWAY FUNCTION IN EFFECT OF DRUG VECTOR
@author: arghanandan
"""
#["lapatilib","AG825","AG1024","U0126","LY294002","temsirolimus"]
def pathway(comb,drugv,inpv,pathv,outv):
    
    #EGFR/ERBB2
    if 1 in comb:
        pathv[0]=1
    else:
        pathv[0]=inpv[0]
        
    if drugv[0]==1 or drugv[1]==1:      #lapatinib/AG825
        pathv[0]=0
        
    #EFGR
    if 2 in comb:
        pathv[1]=1
    else:
        pathv[1]=inpv[0] or inpv[1]
        
    if drugv[0]==1:                     #lapatinib
        pathv[1]=0
        
    #IGFR1A/B
    if 3 in comb:
        pathv[2]=1
    else:
        pathv[2]=inpv[2]
        
    if drugv[2]==1:                     #AG1024
        pathv[2]=0
    
    #ERBB2/3
    if 4 in comb:
        pathv[3]=1
    else:
        pathv[3]=inpv[3]
        
    if drugv[0]==1 or drugv[1]==1:      #lapatinib/AG825
        pathv[3]=0
       
    #GRB2/SOS
    if 5 in comb:
        pathv[4]=1
    else:
        pathv[4]=pathv[0] or pathv[1] or pathv[2] or pathv[3]
        
    #IRS1
    if 8 in comb:
        pathv[5]=1
    else:
        pathv[5]=pathv[2]
    
    #Ras* 
    if 6 in comb:
        pathv[6]=1
    else:
        pathv[6]=pathv[4]
       
    #PTEN changes
    if 7 in comb:
        inpv[4]=0
      
    #MEKK1
    if 13 in comb:
        pathv[7]=1
    else:
        pathv[7]=pathv[6]
    
    #Raf
    if 16 in comb:
        pathv[8]=1
    else:
        pathv[8]=pathv[6]
    
    #PIK3CA*
    if 9 in comb:
        pathv[9]=1
    else:
        pathv[9]=pathv[6] or pathv[5] or pathv[3]
    
    if drugv[4]==1:                     #LY294002
        pathv[9]=0
     
    #MKK4/7
    if 14 in comb:
        pathv[10]=1
    else:
        pathv[10]=pathv[7]
    
    #MEK1
    if 17 in comb:
        pathv[11]=1
    else:
        pathv[11]=pathv[8]
    
    if drugv[3]==1:                     #U0126
        pathv[11]=0
    
    #PIP3    
    if 10 in comb:
        pathv[12]=1
    else:
        pathv[12]=pathv[9] or (int)(not inpv[4])
    
    #JNK1
    if 15 in comb:
        pathv[13]=1
    else:
        pathv[13]=pathv[10]
    
    #ERK1/2
    if 18 in comb:
        pathv[14]=1
    else:
        pathv[14]=pathv[11]
    
    #PDPK1
    if 11 in comb:
        pathv[15]=1
    else:
        pathv[15]=pathv[12]
    
    #AKT
    if 12 in comb:
        pathv[16]=1
    else:
        pathv[16]=pathv[15]
    
    #TSC1/2
    if 20 in comb:
        pathv[17]=0
    else:
        pathv[17]=(int)(not pathv[16])
    
    #GSK3
    if 19 in comb:
        pathv[18]=0
    else:
        pathv[18]=(int)(not pathv[16])
    
    #RHEB
    if 21 in comb:
        pathv[19]=1
    else:
        pathv[19]=(int)(not pathv[17])
    
    #mTOR
    if 22 in comb:
        pathv[20]=1
    else:
        pathv[20]=pathv[19]
    
    if drugv[5]==1:                     #temsirolimus
        pathv[20]=0
        
    #RP6SKB1
    if 23 in comb:
        pathv[21]=1
    else:
        pathv[21]=pathv[14] or pathv[15] or pathv[20]
    
    #BAD
    if 24 in comb:
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