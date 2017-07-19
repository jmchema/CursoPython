# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:33:02 2017

@author: thinktic
"""

"""
#Parte 1
with open("datos_ficheros","r",encoding="UTF-8") as fd:
    linea= fd.readline()
    x=0
    for num in linea.split():
        x= x+ int(num)

print("La suma de los numeros es {}".format(x))

with open("resultado_eje2.txt","w",encoding="UTF-8") as fd:
    sumatorio = " + ".join(linea.split())
    fd.write(sumatorio[:-4])
    fd.write("= "+str(x))


#Pàrte 2
with open("datos_ficheros","a",encoding="UTF-8") as fd:
    linea = "1\r2   3    4   5    6   7   8   9   10"
    print(linea)
    fd.writelines(linea)
    
"""

with open("datos_ficheros", "r", encoding="utf-8") as f_in:
    with open("datos_ficheros_2","w", encoding="utf-8") as f_out:
        for linea in f_in:
            numeros = linea.split()
            
            suma=0
            for numero in numeros:
                suma = suma + int(numeros)
                
            nueva_linea = "{} = {}\n".format(" + ".join(numeros),suma)
            f_out.write(nueva_linea)
            
with open("datos_ficheros","a", encoding="utf-8") as f_out: 
    valores = list(range(1,11))
    valores_cadena = []
    for valor in valores:
        valores_cadena.append(str(valor))
    print(" ".join(valores_cadena))
    f_out.write(" ".join(valores_cadena))
    f_out.write("\n")
    
with open("datos_ficheros", "r", encoding="utf-8") as f_out:
    ultimo = f_out.readline()[-1]
numeros = ultimo.split()
producto = 1 
    
with open("datos_ficheros", "r", encoding="utf-8") as f_out:
    for linea in f_out:
        pass
    ultima = linea
    
    numeros = ultima.split()
    producto = 1
    for numero in numeros:
        producto *= int(numero)
    print(producto)
    
## Dejo de copiar para anteder a la explicacion que sino no me entero
    


