# Listas
# Pueden tener distintos tipos de valores o repetidos

lista = [1, 2, 3, 4, 5, 6.7, "ocho", 9, False, 1]
print(lista)

for cada_elemento in lista:
    print(cada_elemento)

# La funcion append añade un elemento al final de la lista
print("Append")
lista.append(55)
print(lista)

# extend: extiende la lista agregandole otra lista u otro iterable
print("Extend")
lista2 = [0, True, "cero", "0"]
lista.extend(lista2)
print(lista)

# insert: Insertar un elemento en una posicion que le des
print("Insert")
lista.insert(2, 2.5)
print(lista)

# remove: Quitar el primer elemento que encuentre con ese valor
print("Remove")
lista.remove(0)
lista.remove(0)
lista.remove("0")
print(lista)

# pop: Quita el elemento en la posicion que le des y lo devuelve
print("Pop")
lista.pop(-1)
print(lista)
elemento_eliminado = lista.pop(0)
print(elemento_eliminado)

# index: Devuelve el indice del primer elemento que sea igual al que le indiquemos
print("Index")
print(lista.index(2.5))
print(lista.index(3, 2, 4))
# Primer argumento es el dato que buscamos, el segundo puede ser el inicio (opcional) y el tercero el final

# copy: Realizar una copia superficial de una lista - Podemos editar la nueva lista
print("Copy")
lista_copia = lista # Apuntador
lista.append(5)
print(lista_copia)
print(lista)

lista_copia = lista.copy()
lista_copia.pop()
print(lista_copia)

# count: Cuenta cuantas veces el elemento aparece en la lista
print("Count")
lista.append(3)
print(lista)
print(lista.count(3))

# sort: Ordena elementos de una lista
print("Sort")
lista.remove("ocho")
lista.sort()
print(lista)

lista_palabras = ["Mojo", "Python", "PHP", "ADA", "C", "JavaScript", "COBOL"]
lista_palabras.sort()
print(lista_palabras)

# reverse: Invierte la lista
print("Reverse")
lista.reverse()
print(lista)

# clear: Elimina todos los elementos de la lista, no la lista
print("Clear")
lista.clear()
print(lista)