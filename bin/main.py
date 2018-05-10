#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 00:08:33 2018

@author: arghanandan
"""

def main():
    print("\n\n1. Unique input vector")
    print("2. Simulation: single faults")
    print("3. Simulation: double faults")
    print("4. Therapy: single faults")
    print("5. Therapy: double faults")
    print("6. Visualise: single fault therapy (encoded)")
    print("7. Visualise: single fault therapy (condensed)")
    print("8. Visualise: double fault therapy (condensed)")
    print("9. Visualise: combined 1-3")
    print("10.Time: GPU v CPU")
    print("11.Therapy: known v custom")
    print("0. Exit") 
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
    elif n==6:
        import visual_drug1i
    elif n==7:
        import visual_drug1s
    elif n==8:
        import visual_drug2
    elif n==9:
        import visual_combined
    elif n==10:
        import visual_time
    elif n==11:
        import visual_compare
    elif n==0:
        return 0
    
main()