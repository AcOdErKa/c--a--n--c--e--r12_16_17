#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:15:43 2018

@author: arghanandan
"""

#encoding output vector
def encode(output_vector,design_parameter=0.5):
    outv=output_vector
    t=0
    r=0
    a=design_parameter
    for i in range(4):
        t=t+outv[i]
    for i in range(4,7):
        r=r+outv[i]
    return a*(t*r) + (1-a)*(t+r)