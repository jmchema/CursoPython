def es_par(n):
    return n % 2 == 0

print(es_par(2))
print(es_par(3))

l = [2, 3, 44, 32, 27, 99]
l_pares = filter(es_par, l)
print(list(l_pares))

l_impares = filter(lambda n: n % 2 == 1, l)
print(list(l_impares))
suma = lambda x, y: x + y
producto = lambda x, y: x * y
print(suma(5,7))
print(producto(3,7))

l_cuadrado = map(lambda x: x**2, l)
print(list(l_cuadrado))
    