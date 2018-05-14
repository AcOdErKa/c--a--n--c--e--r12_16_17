#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 23:55:18 2018
RETURN ALL POSSIBLE COMBINATIONS OF GIVEN VECTOR
@author: arghanandan
"""

#combination of vector
def combination(vec):
    i=len(vec)-1
    while vec[i]==1:
        vec[i]=0
        i=i-1
    if i==-1:
        return False
    vec[i]=1
    return vec