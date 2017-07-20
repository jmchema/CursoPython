# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:06:10 2017

@author: thinktic
"""

x = [8, 2, 3, 7, 5, 3, 7, 3, 1]

#el mayor de la lista
print("el mayor de la lista es {}".format(max(x)))

#el menor de la lista
print("el menor de la lista es {}".format(min(x)))

# Los tres mayores
print("los 3 mayores de la lista es {}".format(sorted(x,reverse=True)[:3]))

#el mayor de los tres primeros
print("el mayor de los tres primeros {}".format(max(x[:3])))

#el menor de los cuatro ultimos
print("el menor de los cuatro ultimos {}".format(min(x[-5:])))

# Los suma de los 5 mayores
print("Los suma de los 5 mayores es {}".format(sum(sorted(x,reverse=True)[:5])))

#La suma de los tres menores
print("La suma de los tres menores es {}".format(sum(sorted(x)[:3])))
