# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 02:28:13 2025

@author: SamayPC
"""


n = int(input("number od terms "))

# first two terms
n1, n2 = 0, 1
count = 0

if n == 1:
   print(n1,end=" ")

else:
   while count < n:
       print(n1,end=" ")
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1