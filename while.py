# Ciclo while
# Mientras la condicion se cumpla, seguira ejecutandose el ciclo o bucle

contador = 0
while True:
    print("Este es un ciclo infinito", contador)
    contador = contador + 1
    if contador == 1000:
        break

# Funcion eval
# Sirve para evaluar una expresion de cadena como una expresion de Python valida
# Toma una cadena de texto y la evalua como una funcion de Python

cadena = "3 + 4 * 2"
resultado = eval(cadena) # Evalua expresiones matematicas o convierte a una expresion en Python
print(resultado)

numero = 7
while True:
    pregunta = int(input("Adivina el numero: "))
    if pregunta == numero:
        break
print("Has adivinado correctamente")


# El pass no hace nada pero se usa para no dejar algo vacio y no tener error de sintaxis
class Vacia:
    pass