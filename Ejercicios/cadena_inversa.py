"""
Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(cadena):
    lista = list(cadena)
    lista_inversa = []
    i = -1
    for elemento in lista:
        lista_inversa.append(lista[i])
        i = i - 1
    cadena_inversa = "".join(lista_inversa)
    print(cadena_inversa)

cadena = "estoy probando"
inversa(cadena)