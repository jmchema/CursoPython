# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:28:26 2017

@author: thinktic
"""
def anyade(lista,valor):
    return lista.append(valor)

def anyade2(lista,lista2):
    lista = lista +lista2
    print(lista)

# curioso que pueden poner la funciones como "variables"    
lista_funciones = (len, sum, print)
l = [12, 112, 1231, 11]
for function in lista_funciones:
    r = function(l)
    print("{}({}) -> {}".format(function, l, r))