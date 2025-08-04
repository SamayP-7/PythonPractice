# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 02:51:45 2025

@author: SamayPC
"""
is_prime = True
num = int(input("number = "))
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
print(is_prime)