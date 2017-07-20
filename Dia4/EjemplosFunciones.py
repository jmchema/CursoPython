# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:41:21 2017

@author: thinktic
"""

def suma( p1 , p2):
    print(p1)
    print(p2)
    return p1+p2

def num_elementos(secuencia):
    print("La secuencia tiene {} elementos".format(len(secuencia)))
    
def bienvenido (nombre, saludo='Hola', tratamiento="Sr."):
    print("{} , {} {}".format(saludo,tratamiento,nombre))
    
def por_defecto(p1=1, p2=2):
    print(p1)
    print(p2)

"""
No se puede poner parametro sin valor por defecto, obligtorios por detras    
def bienvenida2 (saludo='Hola', tratamiento="Sr.", nombre):
    print("{} , {} {}".format(saludo,tratamiento,nombre))
"""  

def max_y_min(x, y):
    if x > y:
        return x, y
    else:
        return y, x  
    
def max_y_min_2 (l):
    """ Devuielve el maxiom valor de l """
    return max(l), min(l)