"""
De una lista encuentra el par que sume un numero que le des
Que devuelva los dos numeros que suman el numero objetivo

[1, 2, 3]
Objetivo = 3
Resultado = 1, 2
"""

def buscar(lista, objetivo):
    visto = {}
    for numero in lista:
        if objetivo - numero in visto:
            return [objetivo - numero, numero]
        visto[numero] = True
    return []

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(buscar(lista, 19))