#! /usr/bin/env python

""" A partir de dos listas de enteros, 'numeros1' y 'numeros2', almacenar en una
    lista el resultado de multiplicar cada uno de los elementos de 'numeros1'
    por, a su vez, cada uno de los elementos de 'numeros2'. Es decir, la lista
    resultante tendra len(numeros1) * len(numeros2) elementos. """


numeros1 = [1, 7, 13, 21, 27]
numeros2 = [8, 9, 28, 41, 55, 77]

res = []
for n1 in numeros1:
    for n2 in numeros2:
        res.append(n1*n2)

print(res)