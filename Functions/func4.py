# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 12:15:55 2025

@author: SamayPC
"""

def isPrime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    
print(isPrime(1))
print(isPrime(2))
print(isPrime(10))
print(isPrime(47))