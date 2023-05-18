# Se usa junto con el try y el except
# Para asegurarnos que cirtas acciones se realicen sin importar si hay error o no

# try - except - finally

def dividir(a, b):
    try:
        resultado = a / b
        print("El resultado es: ", resultado)
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        print("Finalizando calculo")

dividir(8, 2)
dividir(8, 0)
