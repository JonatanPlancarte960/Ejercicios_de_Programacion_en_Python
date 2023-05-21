# Acciones de limpieza
# Buena practica

def funcion():
    while True:
        try:
            file = open("Manejo de Errores\\testfile.txt", "w")
            edad = int(input("Coloca tu edad: "))
            file.write("Tu edad al cuadrado es: " + str(edad ** 2))
            print("Se ha escrito en el archivo con exito")
            break
        except KeyboardInterrupt:
            print("\nEl usuario ha detenido el programa")
            break

        except IOError:
            print("Hubo un error al escribir un archivo")

        except ValueError:
            print("No introduzcas letras o simbolos, solo numeros")

        finally:
            file.close()

funcion()

print("Adios, vuelve pronto")