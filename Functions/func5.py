# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 11:51:38 2025

@author: SamayPC
"""

def cal_menu(funct,a,b):
    if funct == "add":
        return a+b
    elif funct == "sub":
        return a-b
    elif funct == "mul":
        return a*b
    elif funct =="div":
        return a/b
    elif funct =="mod":
        return a%b
    else:
        pass
    
print("a+b=",cal_menu("add",10,5))
print("a-b=",cal_menu("sub",10,5))
print("a*b=",cal_menu("mul",10,5))
print("a/b=",cal_menu("div",10,5))
print("a%b=",cal_menu("mod",10,5))
    
        
    
    