# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 17:23:37 2017

@author: thinktic
"""

lista = ['primero', 2, "3.5", 4.0, "ultimo"]
print("La logitud de la lista es: %d" % len(lista))
print("el tamaño de lista por el segundo elemento: %d" % (len(lista)*lista[1]))
print("producto del segundo por el tercero: {}".format(lista[1]*float(lista[2])))
print("Esta el numero dos en la lista?", 2 in lista)
print("Esta el numero 2.0 en la lista?", 2.0 in lista)
del lista[0]
print ("Tras eliminar priemra", lista)
del lista[-2:]
print ("Tras eliminar los dos ultimos", lista)
print("Lista con contenido?",bool(lista))
print(lista.append("nuevo ultimo"))
print("Lista con uno más: ",lista)
print("Lista con uno más (con format): {}".format(lista))


