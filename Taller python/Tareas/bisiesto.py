# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:14:43 2022

@author: Christian
"""

def bisiesto(anio):
    
    if (anio%4==0 and anio%100!=0 or anio%400==0):
        return True
    else:
        return False

testData = [1900, 2000, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testData)):
    yr = testData[i]
    print(yr,"-> ",end="")
    result = bisiesto(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
        