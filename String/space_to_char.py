# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 01:31:23 2025

@author: SamayPC
"""

string = input("input string with spaces: ")
char = input("input character to replace space with: ")
s1=""
for c in string:  
    if c != " ":      
        s1 += c
    else:
        s1+=char

print(s1)

print(string.replace(" ", char))