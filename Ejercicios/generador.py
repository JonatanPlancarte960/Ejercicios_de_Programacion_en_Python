"""
Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n, caracter):
    n = int(n)
    caracter = str(caracter)
    resultado = n * caracter
    return resultado

n = 6
caracter = "a"

print(generar_n_caracteres(n, caracter))