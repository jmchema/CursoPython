# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:22:00 2017

@author: thinktic
"""

fd = open("datos_ficheros","r",encoding="UTF-8")
linea= fd.readline()
print("La longitud de la priemra linea es {}".format(len(linea.rstrip())))
#fd.close() Usamos seek(0) para reiniciar la suma y no hace falta cerrar fd

## Nuemro de lineas del fichero
#fd = open("datos_ficheros","r",encoding="UTF-8")
fd.seek(0)
lineas= fd.readlines()
x=0
for linea in lineas:
        x=x+1
fd.close()
print("El numero de lineas {}".format(x))

#Numero la priema liena del fichero
fd = open("datos_ficheros","r",encoding="UTF-8")
linea= fd.readline()
x=0
for c in linea:
    if c in ["1","2","3","4","5","6","7","8","9","0"]:
        x=x+1
fd.close()
print("El numero de lineas {}".format(x))

#Suma de los numero en la priemra linea
with open("datos_ficheros","r",encoding="UTF-8") as fd:
    linea= fd.readline()
    x=0
    for num in linea.split():
        x= x+ int(num)
    #fd.close() con el with no es necesario
    print("La suma de los numeros es {}".format(x))
with open("resultado_eje1.txt","w",encoding="UTF-8") as fd:
    fd.write(str(x))
    #fd.close() 


