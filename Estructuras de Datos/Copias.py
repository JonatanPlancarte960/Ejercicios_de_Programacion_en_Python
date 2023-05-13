# Copia superficial y copia profunda
import copy

print("Copia superficial")
lista1 = [1, 2, 3, [4, 5, [7]]] # Se pueden poner listas dentro de otras

# Las listas internas siguen ligadas
lista1_copia_superficial = lista1.copy()

# Las listas internas no estan ligadas, es como si redeclararas la variable
lista1_copia_profunda = copy.deepcopy(lista1)

lista1.append(8)
lista1[3].append(6) # La lista padre esta separada pero la lista hijo sigue referenciada a la lista original
lista1[3][2].append(8)

print(lista1)
print(lista1_copia_superficial)
print(lista1_copia_profunda)

