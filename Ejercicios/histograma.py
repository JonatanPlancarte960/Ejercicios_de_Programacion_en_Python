"""
Definir un histograma_procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
"""

def histograma_procedimiento(lista_numeros):
    for elemento in lista_numeros:
        print(elemento * "*")

lista_numeros = [4, 9, 7, 9, 10, 100, 9]
histograma_procedimiento(lista_numeros)