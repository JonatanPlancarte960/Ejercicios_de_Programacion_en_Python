# El ciclo for
palabras = ["gato" , "perro" , "manzana"]
for palabra in palabras: # Para cada palabra dentro de palabras:
    print(palabra, len(palabra)) # Imprime palabra, longitud de palabra
    # Palabra es un iterador, for i in lista:
    # len sirve para dar la cantidad de elementos que tiene una cadena

print("---------------------------------------------------------------")
varias_palabras = []
num_palabras = 0
num_palabras = int(input("¿Cuantas palabras quieres ingresar? "))

# Si se necesita iterar sobre una secuencia de numeros usamos la funcion range
# Range() genera numeros del cero al numero que especifiques -1

for i in range(num_palabras): # Para cada i(iterador - variable temporal) en un rango de num_palabras(el numero que el usuario especifique - 1)
    print("Palabra ", i + 1, " - Te quedan ", num_palabras - i - 1) # Imprime Palabra i Te quedan num_palabras - i
    palabra_usuario = input("Introduce la palabra: ") # palabra_usuario es igual a la palabra que el usuario ingrese
    varias_palabras.append(palabra_usuario) # La lista varias_palabras.append agrega palabra usuario(la palabra que el usuario ingrese)
    # append() sirve para añadir una cadena a una lista
print("Este es el resultado") # Imprime Este es el resultado
print(varias_palabras) # Imprime la lista varias_palabras

print("---------------------------------------------------------------")
# Checador de numeros primos
# Un numero primo es el que solo se divide entre si mismo y entre uno

for n in range(2, 10): # Genera un rango del 2 al 10, contando el 2 pero sin llegar al 10
    # Para cada n en un rango de 2 a 10, contando el 2 pero sin llegar al 10

    # (2,3,4,5,6,7,8,9)

    es_primo = True # es_primo es igual a True al entrar al primer ciclo for

    for x in range(2, n): # Para cada x en un rango de 2 a n pero sin llegar a n

    # (2,3,4,5,6,7,8,9)
        if n % x == 0: # Si el residuo de n / x es igual a 0 entonces
            es_primo = False # es_primo es igual a False
            break # Se rompe el segundo bucle for

    if es_primo and n != 2: # Si es primo igual a True entonces
        print(n, "Es numero primo") # Imprime n Es numero primo

    else: # Si no
        print(n, "No es numero primo") # Imprime n No es numero primo

print("---------------------------------------------------------------")
# Continue
# Detector de pares e impares
for num in range(2,10):
    if (num % 2 == 0):
        print(num, "Es par")
        continue
    print(num, "Es impar")