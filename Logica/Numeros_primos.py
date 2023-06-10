"""
Verificar si un numero es primo

A que solo sea divisible entre si mismo y el 1
"""

def es_primo(numero):
    if numero < 2: # 1 y 0 no son primos
        return False
    for i in range(2, int(numero)):
        if numero % i == 0:
            print(numero, "/", i, "=", (numero / i))
            return False
    return True

print(es_primo(6))