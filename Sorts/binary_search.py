def busqueda_binaria(lista, valor):
    low = 0
    high = len(lista) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if lista[mid] < valor:
            low = mid + 1

        elif lista[mid] > valor:
            high = mid - 1
        
        else:
            return mid
        
    return -1

lista = [2, 5, 6, 7, 90, 110]

valor = 5

resultado = busqueda_binaria(lista, valor)

if resultado != -1:
    print("El elemento esta en el indice", resultado)

else:
    print("El elemento no se encuentra en la lista")