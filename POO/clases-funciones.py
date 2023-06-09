# Clases
# Fundamentos de programacion orientada a objetos
# Clase - Objeto

"""
Existen cuatro tipos de notacion

Camel Case -> contarElementos - Variables y Funciones, Java, JS, PHP, Swift

Pascal Case -> ContarElementos - Nombres de Clases, JS, PHP, Java

Snake Case -> contar_elementos - Variables y Funciones en Python, C

Kebab Case -> contar-elementos - URL
"""

class Persona:
    # Primero los atributos de la clase
    edad = 0
    nombre = ""

    # Constructor
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    # La palabra reservada def sirve para definir una funcion
    
    def leer_edad(self):
        # Scope - Global, Modulo, Clase, Local 
        # self -> esta clase
        return self.nombre + " tiene " + str(self.edad) + " años"
        # Return es una palabra reservada de la funcion, nos permite que se acabe la funcion de la ejecucion y devuelve algo

jonatan = Persona("Jonatan", 19, 1.63)
print(jonatan.leer_edad())
print(jonatan.altura)

mari = Persona("Mari", 25, 1.60)
print(mari.leer_edad())
print(mari.altura)

print("---------------------------")
# ---------------- Otra Funcion --------------------------

class Perro:
    tipo = "Canino" # Variable va a ser compartida con todas las instancias
    def __init__(self, nombre):
        self.nombre = nombre
        self.trucos = []

    def aprender_truco(self, truco):
        self.trucos.append(truco)

puppy = Perro("Puppy")
puppy.aprender_truco("Dar la patita")

manchas = Perro("Manchas")
manchas.aprender_truco("Hacerce el muertito")

print(puppy.tipo)
print(manchas.tipo)

print(puppy.nombre)
print(manchas.nombre)

print(puppy.trucos)
print(manchas.trucos)