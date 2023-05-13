# List comprehension
# Es una manera consisa de crear listas

cuadrados = [] # Esto va a contener los numeros al cuadrado
for numero in range(10):
    cuadrados.append(numero**2)

print(cuadrados)

cuadrados2 = list(map(lambda numero: numero**2, range(10)))
print(cuadrados2)

cuadrados3 = [numero**2 for numero in range(10)]
print(cuadrados3)