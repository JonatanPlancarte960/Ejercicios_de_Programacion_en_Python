# Conjuntos o sets
"""
Es una coleccion no ordenada y sin elementos repetidos

Operaciones logicas como union, interseccion, diferencia...
"""

frutas = {'Manzana', 'Naranja', 'Pera', 'Manzana', 'Naranja', 'Platano'}
print(frutas)

palabra = {'abracadabra'}
palabra1 = set('abracadabra')
print(palabra1)

lista_frutas = ['Manzana', 'Naranja', 'Pera', 'Manzana', 'Naranja', 'Platano']
lista_frutas = list(set(lista_frutas))
lista_frutas.sort()
print(lista_frutas)

print('Naranja' in frutas)
print('Uva' in frutas)

for elemento in frutas:
    print(elemento)

palabra1 = set('abracadabra')
palabra2 = set('alacazam')

print(palabra1)
print(palabra2)

# Diferencia con conjuntos
print(palabra1 - palabra2) # Todas las letras que esten en palabra1 pero no es palabra2
print(palabra2 - palabra1)

# Union
print(palabra1 | palabra2) # Todas las letras que esten en palabra1 y en palabra2 o ambas y si repetir

# Interseccion
print(palabra1 & palabra2) # Todas la letras que esten en ambos conjuntos

# Diferencia simetrica
print(palabra1 ^ palabra2) # Todas las letras que esten en palabra1 y en palabra2 pero no en ambas

# Comprension de conjuntos
a = {elemento for elemento in 'abracadabra' if elemento not in 'abc'}
print(a)