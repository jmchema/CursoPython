# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:07:53 2017

@author: thinktic
"""

##Palindromo
frase = input("Meter lafrase: ")
print("La cadena metida es {}".format(frase))
print("La cadena metida invertida {}".format(frase[::-1]))
frase=frase.lower().replace(' ','').strip()
if frase == frase[::-1]:
    print("Es palindromo")
else:
    print("No es palindromo")


