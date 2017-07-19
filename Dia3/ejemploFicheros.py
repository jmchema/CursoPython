# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:47:27 2017

@author: thinktic
"""


print("Leer de un golpe")
# fd = open("primerFichero.txt","r",encoding="UTF-8") 
#Tambien valido perocodificacion por defecto
fd = open("primerFichero.txt","r",encoding="UTF-8")
print(fd.read())
fd.close()

print("Por lineas")
fd = open("primerFichero.txt","r",encoding="UTF-8")
linea = "--"
while linea:
    linea = fd.readline()
    print(linea.rstrip())
fd.close()

print("Otra forma")
fd = open("primerFichero.txt","r",encoding="UTF-8")
lineas= fd.readlines()
for linea in lineas:
        print(linea.rstrip())
fd.close()

print("Version 3")
fd = open("primerFichero.txt","r",encoding="UTF-8")
for linea in fd:
    print(linea.rstrip())
fd.close()

print("Ejemplos escritura")
fd = open("otroFichero.txt","w",encoding="UTF-8")
fd.write("Hola esta es una prueba de escritura")
fd.write("\n")
fd.write("Otra linea")
fd.close()

print("Ejemplo machacar")
fd = open("otroFichero.txt","w",encoding="UTF-8")
fd.write("Machaco lo de antes")
fd.write("\n")
fd.write("Otra linea")
fd.close()

print("Ejemplo de continuar lo que hay")
fd = open("otroFichero.txt","a",encoding="UTF-8")
fd.write("\nMeto una linea extra")
fd.write("\n")
fd.write("Un bís")
fd.close()

print("Mas ejemplo de lectura con split")
fd = open("primerFichero.txt","r",encoding="UTF-8")
for linea in fd:
    for palabra in linea.split():
        print(palabra)
fd.close()


    