x = [8, 2, 3, -1, 2, -5, 7]
personas = ["Sara", "Pedro", "Miguel"]

# El cudo de cada elemento de la lista
l_cubo = [a ** 3 for a in x]
print(list(l_cubo))

l_cua_imp = [a ** 3 for a in x if a % 2 == 1]
print(list(l_cua_imp))

# El cuadrado de los elementos pares y positivos de x.
l_cua_par_pos = [a ** 2 for a in x if (a % 2 == 0) and a>0]
print(list(l_cua_par_pos))

# Los elementos de personas con m ́as de cinco caracteres.
l_mas5 = [a for a in personas if len(a)>5]
print(list(l_mas5))

linea = "123 234 132 1 342 21 12 123 4"
numeros = linea.split()
suma = sum([int(v) for v in numeros])
print(suma)

dico = {persona: len(persona) for persona in personas}
print("La longitud de la cadena {} es {}".format("Sara",dico["Sara"]))
print(dico)

l_salida = []
for persona in personas:
    l_salida.append( (persona.lower(), len(persona)) )
    print("Nuevo valor")
    
tuplas = [(persona.lower(), len(persona)) for persona in personas]
print(tuplas)
