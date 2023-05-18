import sys

try:
    archivo = open("Manejo de Errores\\archivo.txt", "r")
    texto = archivo.readline()
    i = texto.strip()

except OSError as error:
    print("OSError", error)
except ValueError as error:
    print("No se pueden convertir los datos", error)
except Exception as error:
    print("Error no conocido", error)
    raise
finally:
    archivo.close()

print(texto)