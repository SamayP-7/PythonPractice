# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 12:01:47 2025

@author: SamayPC
"""

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
    
print("6! =",fact(6))

def per_cal(*marks, tot_1 = 100):
    total=0
    for i in marks:
        total+=i
    per = total/(tot_1*len(marks))*100
    return total,per

total,per = per_cal(80,90,100)
print(total,per)

t1,p1 = per_cal(80,90)
print(t1,p1)