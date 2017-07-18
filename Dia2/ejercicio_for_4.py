#! /usr/bin/env python

""" A partir de dos listas de enteros, 'numeros1' y 'numeros2', crea una lista
    que contiene aquellos valores de la primera que tambien estan en la segunda
    e imprimela por pantalla. Es decir, calcula la interseccion de ambas listas. """


numeros1 = [1, 7, 13, 21, 27, 29, 34, 48, 50, 51, 53, 61, 68, 74, 82, 83, 84, 87, 92, 94]
numeros2 = [4, 6, 10, 18, 23, 29, 30, 32, 43, 54, 55, 55, 71, 76, 77, 82, 88, 92, 94, 95]

resultado = []
for i in range(len(numeros1)):
    resultado.append(numeros1[i]*numeros2[i])
    
print(resultado)

# Otra forma mejor

resultado = []
for n1,n2 in zip(numeros1,numeros2):
    resultado.append(n1*n2)
print(resultado)

# Tres dimnensiones
resultado2 = []
for n1,n2,n3 in zip(numeros1,numeros2,resultado):
    resultado2.append(n1*n2*n3)
print(resultado2)

