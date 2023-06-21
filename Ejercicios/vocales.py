"""
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

def vocales(caracter):
    if caracter in "aeiou":
        return True
    else:
        return False
    
caracter = "a"

print(vocales(caracter))