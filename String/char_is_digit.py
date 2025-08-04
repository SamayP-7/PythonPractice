# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 01:26:18 2025

@author: SamayPC
"""
ch = input("input char: ")

if(ch >= '0' and ch <= '9'):
    print("Digit")
else:
    print("Not a Digit")
    
print(ch.isdigit())
