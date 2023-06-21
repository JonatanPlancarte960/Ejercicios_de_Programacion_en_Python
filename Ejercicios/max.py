"""
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def max(numero_1, numero_2):
    if numero_1 > numero_2:
        print(f"El numero {numero_1} es mas grande que el numero {numero_2}")
    
    elif numero_2 > numero_1:
        print(f"El numero {numero_2} es mas grande que el numero {numero_1}")

    else:
        print(f"El numero {numero_1} es igual al numero {numero_2}")

numero_1 = 10
numero_2 = 5

max(numero_1, numero_2)