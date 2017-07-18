# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 19:05:45 2017

@author: thinktic
"""
print("Ejecicio Uno")
i=0
while True:
    i= i + 1
    if (i**2 >= 2048):
        break
    else:
        print("Ptencia de 2 de {}->{} ".format(i,i**2))
"""        
print("Ejericcio 2: leer hasta numero par")
x = 1
while x % 2 != 0  :
    x = int(input("Introduce un numero:"))
    print("Con {} seguimos".format(x))
"""
print("ejecicio 3: 15 priemra potencias de 3")
for i in range(16):
    print("Potencia de 2 de {}->{} ".format(i,i**2))
    
print("Ejecicio 4")
cadena = input("Introduzca una palabra: ")
for valor in cadena:
    if valor.lower() in "aeiou":
        print("{} es una vocal".format(valor))
    else:
        print("{} no es una vocal".format(valor))
    
print("Ejercicio 5")
numeros1=[1,2,3,4]
numeros2=[10,2,23,3,5]
res=[]
for valor in numeros1:
    if valor in numeros2:
        res.append(valor)
print(res)
    
