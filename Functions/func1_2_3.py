# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 11:35:08 2025

@author: SamayPC
"""

def person (name,age):
    print(f"name: {name} age: {age}")
    
person("abc",20)

def calculation(a,b):
    return a+b, a-b

a = 10
b =5

c,d = calculation(a,b)
print(f"a+b = {c}\na-b = {d}")


def show_employee(name,salary=9000):
    print(f"name: {name}\nSalary: {salary}")

show_employee("abc",5000)
show_employee("xyz")