# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:18:22 2022

@author: Christian
"""

def fibonacci(n):
    a=1
    b=1
    if n==1:
        print('0')
    elif n==2:
        print('0','1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n-4):
            total = a + b
            b=a
            a= total
            print(total)
         

