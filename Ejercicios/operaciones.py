"""
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def sum(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        suma = suma + numero
    print(suma)

def multip(lista_numeros):
    multiplicacion = 1
    for numero in lista_numeros:
        multiplicacion = multiplicacion * numero
    print(multiplicacion)

lista_numeros = [1, 2, 3, 4, 5]

sum(lista_numeros)
multip(lista_numeros)