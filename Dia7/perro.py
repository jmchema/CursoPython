class Perro(object):   #Object es la clase de la que deriva, todas nacen en Object. En Py2 era oblgatorio en Py3 no

    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladra(self):
        print (self.nombre, "dice 'Wooof!'") #En python 2 no habia () en el print
    
mascota = Perro("Lassie", "Collie", 18)
mascota.ladra()
