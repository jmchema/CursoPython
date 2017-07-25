"""
Definimos esta estructura:

        Animal
        /    \
    Persona  AnimalSalvaje
        \       /
        HombreLobo
 
"""

"""
class Animal:
    def __init__(self):
        print("Iniciando al animal...")
        self.esta_vivo=True
        
class Persona(Animal):
    def __init__(self,nombre):
        print("Iniciando a la persona....")
        Animal.__init__(self)
        self.nombre = nombre

class AnimalSalvaje(Animal):
    def __init__(self, especie):
        print("Iniciando a un animal salvaje")
        Animal.__init__(self)
        self.especie = especie

# Hombre lobo cojo la hencia de dos clases que cuelgan de un padre, Animal
# por lo que esto hace que animal se ejecute dos veces. Lo cual puede ser un
# problema. Como por ejemplo los socket.


class HombreLobo(Persona, AnimalSalvaje):
    def __init__(self, nombre,especie):
        print("Iniciando al hombre lobo")
        Persona.__init__(self, nombre)
        AnimalSalvaje.__init__(self,especie)
"""
# Tenemos dos posibles soluciones. Llamar a init de un orden que no tenga
# mas de un camino... no siempre posible... O la mejor opción, usar super
# Lo hacemos super. Super es muy listo y  sabe hacer la inicializacion unica
# el solito. Es un patada a seuir y nos despreocupamos

class Animal:
    def __init__(self, nombre, especie):
        print("Iniciando al animal...")
        self.esta_vivo=True
        
class Persona(Animal):
    def __init__(self, nombre, especie):
        print("Iniciando a la persona....")
        super().__init__(nombre, especie)
        self.nombre = nombre

class AnimalSalvaje(Animal):
    def __init__(self, nombre, especie):
        print("Iniciando a un animal salvaje")
        super().__init__(nombre, especie)
        self.especie = especie


class HombreLobo(Persona, AnimalSalvaje):
    def __init__(self, nombre,especie):
        print("Iniciando al hombre lobo")
        super().__init__(nombre, especie)
        
class Roboot:
    def __init__(self, nombre, especie):
        print("Iniciando al root")
        super().__init__(nombre,especie)
        # Aunque robot no hereda de nadie hay que el super,
        # Xq sino se rompe la cadena y no sigue la herencia.
        
class Robocop(Robot, Persona):
    def __init__(self,nombre,especie):
        print("Iniciando robocop")
        super().__init__(nombre,especie)

