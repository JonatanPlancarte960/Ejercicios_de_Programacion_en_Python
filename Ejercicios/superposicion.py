"""
Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
Escribir la función usando el bucle for anidado.
"""

def superposicion(lista_1, lista_2):
    for elemento_i in lista_1:
        for elemento_j in lista_2:
            if elemento_i == elemento_j:
                return True
    return False

lista_1 = [2, 1, 3, 1, 5]
lista_2 = [8, 9, 0, 112, 1]

print(superposicion(lista_1, lista_2))