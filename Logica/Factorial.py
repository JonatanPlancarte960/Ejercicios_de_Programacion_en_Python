"""
Factorial de un numero

Es un numero no negativo "n!" es el producto de todos los numeros entreros positivos de 1 hasta n

La multiplicacion de todos los numeros entreros desde 1 hasta n
"""

# Recursion
def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    
print(factorial(5))

# Con lambda y reduce

# Lambda es una forma de hacer funciones anonimas, es decir funciones sin nombre y de una sola linea

from functools import reduce

def factorial_1(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, numero + 1))
    
print(factorial_1(5))

numeros = [10, 4, 12]
factoriales = [factorial_1(n) for n in numeros]

print(factoriales)
factoriales.clear()

for n in numeros:
    factoriales.append(factorial_1(n))

print(factoriales)

factoriales = list(map(factorial_1, numeros))
print(factoriales)