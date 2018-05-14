#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 00:08:33 2018

@author: arghanandan
"""

def main():
    print("\n\n1. Visualise: single fault therapy (encoded)")
    print("2. Visualise: double fault therapy (encoded)")
    print("3. Visualise: single fault therapy (condensed)")
    print("4. Visualise: double fault therapy (condensed)")
    print("5. Visualise: combined 1-3")
    print("6. Time: GPU v CPU")
    print("7. Therapy: known v custom")
    print("0. Exit")
    n=int(input("Option: "))
    if n==1:
        import visual_drug1i
    elif n==2:
        import visual_drug2i
    elif n==3:
        import visual_drug1s
    elif n==4:
        import visual_drug2s
    elif n==5:
        import visual_combined
    elif n==6:
        import visual_time
    elif n==7:
        import visual_compare
    elif n==0:
        return 0
    
while True:
    n=main()
    if n==0:
        break
