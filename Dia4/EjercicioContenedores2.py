# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:57:31 2017

@author: thinktic
"""

x = [8, 2, 3, 2, 2]
y = [8, 2, 3, 2, 9]

#  ¿Cuantos elementos hay en x si se eliminan los repetidos?
print(len(set(x)))

# Una lista que contenga la concatenaci´on de ambas listas.
lista_x_y= x + y
print(lista_x_y)

#Una lista que contenga la uni´on de ambas listas, sinduplicados.
l= list(set(x).union(set(y)))
print(l)

# 4 Un conjunto que tenga la intersecci´on de ambas listas
c = set(x).intersection(set(y))
print(c)

# 5 Un diccionario en el que para cada entero de la lista x se
# almacena su cuadrado.

cuadrados = {}
for i in x:
    cuadrados[i]=i**2
print(cuadrados)

# Un diccionario en el que se almacena el n´umero de veces
# que cada entero aparece en la lista y.
apariciones = {}
for i in y:
    apariciones[i]=0
for i in y:
    apariciones[i]=apariciones[i]+1
print(apariciones)

# con excepciones el ultimo ejecricio
cont = {}
for v in y:
    try:
        cont[v] += 1
    except KeyError:
        cont[v] = 1
print(cont)
