# Tuplas
# Una tupla es una secuencia de datos o grupo de datos, pueden ser anidadas, tener muchos tipos de datos 
# Es inmutable - se definen con parentesis

tupla1 = (12345, 3.1416, 'Hola', True)
lista1 = [12345, 3.1416, 'Hola', True]

print(tupla1[1])

super_tupla = tupla1, (1, 2, 3, 4, 5), [7, 8, 1]

print(super_tupla)

lista1[1] = 'c'
print(lista1)

super_tupla[2][0] = 'c'
print(super_tupla)

super_lista = list(super_tupla)
print(super_lista)

vacia = ()

# Singleton
# Se usa pare restringir la creacion de una clase a una sola instancia y proporcionar un punto de acceso global a esa instancia unica
# Permite que una clase solo permita la cracion de un objeto de si misma

singleton = 'hola',
print(vacia)
print(singleton)

