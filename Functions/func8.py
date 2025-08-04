# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 12:11:16 2025

@author: SamayPC
"""

def login_fun(user,pwd):
    return True if user == 'admin' and pwd == 'admin@123' else False

print(login_fun("admin", "admin@123"))
print(login_fun("xyz", "admin@123"))
print(login_fun("admin", "admin23"))