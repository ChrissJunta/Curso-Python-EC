# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:19:24 2022

@author: Christian
"""
testanios = [1900, 2000, 2016, 1987]
testMeses = [ 2, 2, 1, 11]
testResults = [28, 29, 31, 30]
def leapanio(anio):
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True
 
def mesanio(anio, mesNumber):
    if anio <= 1582:
        return print(f'{anio} - {None} - el anio no esta declarado hasta esa fecha.')
    elif mesNumber <= 0 or mesNumber > 13:
        return print(f'{mesNumber} - {None} - Debe estar entre 1 y 12')
    else:
        numerodeDiasPormes = [31,28,31,30,31,30,31,31,30,31,30,31]
        res = numerodeDiasPormes[mesNumber-1]
        if mesNumber == 2 and leapanio(anio) == True:
            res = 29
        return res
 
for i in range(len(testanios)):
    anio = testanios[i]
    mes = testMeses[i]
    dias = mesanio(anio,mes)
    if dias == testResults[i]:
        print({'anio': anio,'numero de mes': mes,'Numero de dias': dias})
    else:
        print('Genial.')