# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 01:36:53 2025

@author: SamayPC
"""

string = input("input string: ")
print(string.upper())

s1=""
s2=""
count_vowel=0
count=0
for c in string:  
    if c in "aeiou":      
        s1 += c.upper()
        s2 += ""
        count_vowel+=1
    else:
        s1+=c
        s2+=c
        count+=1
print(s1)

print(s2)
count_cons = count - string.count(" ")
print(f"vowel count = {count_vowel}\nconsonent count = {count_cons}")