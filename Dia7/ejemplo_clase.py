class Persona:
    
    #Incializador. Mas bien el constructor que se diria
    def __init__(self, _nombre, _apellidos, _edad=None):
        self.nombre = _nombre
        self.apellidos = _apellidos
        self.edad = _edad
    
    def hola(self):   #el self hace las funciones de this, pero en python es explicito y no implicito
        print("Hola {} {}".format(self.nombre, self.apellidos))
    
    def adios(self, parametro):
        print("Adios {} {}".format(self.nombre, self.apellidos))
        print("{}".format(parametro))
        
juan= Persona("Juan", "Pérez")
pedro = Persona("Pedro","Gonzalez")