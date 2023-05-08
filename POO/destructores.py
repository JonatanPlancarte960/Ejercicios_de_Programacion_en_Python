# Existen dentro de Python los constructores y destructores
# Los destructores se usan para hacer limpieza y liberacion de recursos de un objeto cuando ya no es usado

class Archivo:
    def __init__(self, nombre_archivo):
        self.archivo = open(nombre_archivo, 'w') # Con la funcion open() se abre un archivo

    def __del__(self):
        self.archivo.close()

archivo_instancia = Archivo("POO\ejemplo.txt")
archivo_instancia.archivo.write("Youtube: OX I Jonatan")
del archivo_instancia # Con el operador del se elimina una instancia