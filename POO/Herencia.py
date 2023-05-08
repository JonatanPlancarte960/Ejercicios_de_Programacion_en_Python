# Herencia
# Un objeto es algo que tiene funciones y atributos
# Hay atributos compartidos y atributos especificos por objeto

# Las clases en Python no llevan parentesis a menos que hagas una herencia
class Figura: # Esta seria la clase padre
    """
    Define una figura segun su base y altura
    """

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Poligono:

    def dar_nombre(self, nombre):
        return f"Esto es un {nombre}"

class Rectangulo(Figura, Poligono):

    def calcular_area(self): # Este es un metodo o una funcion
        return self.base * self.altura
    
class Triangulo(Figura):
    
    def calcular_area(self): 
        return (self.base * self.altura) / 2
    
rectangulo = Rectangulo(20, 5)
triangulo = Triangulo(20, 20)

print("Area del rectangulo: ", rectangulo.calcular_area())
print("Area del triangulo: ", triangulo.calcular_area())

print(rectangulo.dar_nombre("Rectangulo"))