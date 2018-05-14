#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 20:25:28 2018
OBJECTIVE: NETWORK PATHWAY FUNCTION IN EFFECT OF CUSTOM DRUG LOCATIONS
@author: arghanandan
"""

def pathway(comb,drugv,inpv,pathv,outv):
    
    #EGFR/ERBB2
    if 1 in comb:
        pathv[0]=1
    else:
        pathv[0]=inpv[0]
        
    if "DRG1" in drugv:
        pathv[0]=0
        
    #EFGR
    if 2 in comb:
        pathv[1]=1
    else:
        pathv[1]=inpv[0] or inpv[1]
        
    if "DRG2" in drugv:
        pathv[1]=0
        
    #IGFR1A/B
    if 3 in comb:
        pathv[2]=1
    else:
        pathv[2]=inpv[2]
        
    if "DRG3" in drugv:
        pathv[2]=0
    
    #ERBB2/3
    if 4 in comb:
        pathv[3]=1
    else:
        pathv[3]=inpv[3]
        
    if "DRG4" in drugv:
        pathv[3]=0
              
    #GRB2/SOS
    if 5 in comb:
        pathv[4]=1
    else:
        pathv[4]=pathv[0] or pathv[1] or pathv[2] or pathv[3]
    
    if "DRG5" in drugv:
        pathv[4]=0
        
    #IRS1
    if 8 in comb:
        pathv[5]=1
    else:
        pathv[5]=pathv[2]
        
    if "DRG6" in drugv:
        pathv[5]=0
    
    #Ras* 
    if 6 in comb:
        pathv[6]=1
    else:
        pathv[6]=pathv[4]
        
    if "DRG7" in drugv:
        pathv[6]=0
       
    #PTEN changes
    if 7 in comb:
        inpv[4]=0
        
    if "DRG8" in drugv:
        inpv[4]=1
      
    #MEKK1
    if 13 in comb:
        pathv[7]=1
    else:
        pathv[7]=pathv[6]
        
    if "DRG9" in drugv:
        pathv[7]=0
    
    #Raf
    if 16 in comb:
        pathv[8]=1
    else:
        pathv[8]=pathv[6]
    
    if "DRG10" in drugv:
        pathv[8]=0
    
    #PIK3CA*
    if 9 in comb:
        pathv[9]=1
    else:
        pathv[9]=pathv[6] or pathv[5] or pathv[3]
        
    if "DRG11" in drugv:
        pathv[9]=0
    
    #MKK4/7
    if 14 in comb:
        pathv[10]=1
    else:
        pathv[10]=pathv[7]
        
    if "DRG12" in drugv:
        pathv[10]=0
    
    #MEK1
    if 17 in comb:
        pathv[11]=1
    else:
        pathv[11]=pathv[8]
        
    if "DRG13" in drugv:
        pathv[11]=0
   
    #PIP3    
    if 10 in comb:
        pathv[12]=1
    else:
        pathv[12]=pathv[9] or (int)(not inpv[4])
        
    if "DRG14" in drugv:
        pathv[12]=0
    
    #JNK1
    if 15 in comb:
        pathv[13]=1
    else:
        pathv[13]=pathv[10]
    
    if "DRG15" in drugv:
        pathv[13]=0
    
    #ERK1/2
    if 18 in comb:
        pathv[14]=1
    else:
        pathv[14]=pathv[11]
        
    if "DRG16" in drugv:
        pathv[14]=0
    
    #PDPK1
    if 11 in comb:
        pathv[15]=1
    else:
        pathv[15]=pathv[12]
    
    if "DRG17" in drugv:
        pathv[15]=0
    
    #AKT
    if 12 in comb:
        pathv[16]=1
    else:
        pathv[16]=pathv[15]
        
    if "DRG18" in drugv:
        pathv[16]=0
    
    #TSC1/2
    if 20 in comb:
        pathv[17]=0
    else:
        pathv[17]=(int)(not pathv[16])
        
    if "DRG19" in drugv:
        pathv[17]=0
    
    #GSK3
    if 19 in comb:
        pathv[18]=0
    else:
        pathv[18]=(int)(not pathv[16])
        
    if "DRG20" in drugv:
        pathv[18]=0
    
    #RHEB
    if 21 in comb:
        pathv[19]=1
    else:
        pathv[19]=(int)(not pathv[17])
        
    if "DRG21" in drugv:
        pathv[19]=0
    
    #mTOR
    if 22 in comb:
        pathv[20]=1
    else:
        pathv[20]=pathv[19]
        
    if "DRG22" in drugv:
        pathv[20]=0
        
    #RP6SKB1
    if 23 in comb:
        pathv[21]=1
    else:
        pathv[21]=pathv[14] or pathv[15] or pathv[20]
        
    if "DRG23" in drugv:
        pathv[21]=0
    
    #BAD
    if 24 in comb:
        pathv[22]=0
    else:
        pathv[22]=(int)(not(pathv[21] or pathv[16]))
        
    if "DRG24" in drugv:
        pathv[22]=0
    
    outv[0]=pathv[13] and pathv[21]
    outv[1]=pathv[14]
    outv[2]=pathv[14] and pathv[21]
    outv[3]=pathv[14] and pathv[21]
    outv[4]=(int)(not pathv[22])
    outv[5]=(int)(not pathv[22])
    outv[6]=(int)(not pathv[18])