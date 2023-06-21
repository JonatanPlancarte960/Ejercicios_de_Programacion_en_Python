import random

# Para grandes cantidades de tiempo tarda demasiado

def metodo_burbuja(lista):
    longitud_lista = len(lista)

    cambio = True

    while cambio:
        # Creamos una bandera
        cambio = False

        for i in range(longitud_lista - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                cambio = True
    print(lista)

lista = [random.randint(0, 100) for _ in range(10)]
print(lista)

metodo_burbuja(lista)