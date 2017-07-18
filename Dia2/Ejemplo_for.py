# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:13:30 2017

@author: thinktic
"""
# Bucle for en python
for valor in ["hola","a","todos"]:
        print("Un elemento: {}".format(valor))
 
# For de los antiguos. intentar no usar
lista = ["hola","a","todos"]       
for i in range(len(lista)):
    print("Un elemento: {}".format(lista[i]))
 
secuencia = "Vanesa"    
for idx,valor in enumerate(secuencia):
        print("Un elemento: {} -> {}".format(idx,valor))