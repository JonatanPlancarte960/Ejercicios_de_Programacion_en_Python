"""
Definir una función que calcule la longitud de una lista o una cadena dada.
(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def longitud_cadena(cadena):
    numero_letras = 0
    for letra in cadena:
        numero_letras = numero_letras + 1
    print(numero_letras)

longitud_cadena(["a", "b", "c", "d", "e", "f"])
longitud_cadena("abcdef")