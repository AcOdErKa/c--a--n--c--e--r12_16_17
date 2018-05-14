#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 00:08:33 2018

@author: arghanandan
"""

def main():
    print "\n\n1. Unique input vector"
    print "2. Simulation: single faults"
    print "3. Simulation: double faults"
    print "4. Therapy: single faults"
    print "5. Therapy: double faults"
    print "0. Exit"
    n=int(input("Option: "))
    if n==1:
        import fault_zero
    elif n==2:
        import fault_one
    elif n==3:
        import fault_two
    elif n==4:
        import drug_one
    elif n==5:
        import drug_two2
    elif n==0:
        return 0
    
while True:
    n=main()
    if n==0:
        break
