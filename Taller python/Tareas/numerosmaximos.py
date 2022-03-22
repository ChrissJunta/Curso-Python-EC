# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 18:54:56 2022

@author: Christian
"""

def readint(prompt, min, max):

    try:
        prompt = int(input())
        if prompt < min or prompt > max:
            print("Error: el valor no está dentro del rango permitido ")
            return readint(print("Ingresa un numero de -10 a 10: " , end=''), -10, 10)
     
    except ValueError:
        print("Error al ingresar los datos requeridos")
        return readint(print("Ingresa un numero de -10 a 10: " , end=''), -10, 10) 
    
    else:
        return prompt


v = readint(print("Ingresa un numero de -10 a 10: " , end=''), -10, 10)

print("El numero es:", v)
