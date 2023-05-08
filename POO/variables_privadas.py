# Variables privadas

class Mapping:

    def __init__(self, objeto_iterable):
        self.lista = []
        self.__actualizar(objeto_iterable)

    def actualizar(self, objeto_iterable): # Esta es una funcion privada
        for item in objeto_iterable:
            self.lista.append(item)

    __actualizar = actualizar # actualizar es una variable privada
    
class MappingSubClass(Mapping):
    
    def actualizar(self, keys, values):
        for item in zip(keys, values):
            # El zip combina dos o mas iterables o listas en una sola lista
            self.lista.append(item)

instancia = MappingSubClass(['a', 'b', 'c', 'd', 'e', 'f'])
instancia.actualizar(['key1'], ['value1'])
print(instancia.lista)

numeros = [1, 2, 3, 4, 5]
colores = ['rojo', 'verde', 'negro', 'azul', 'amarillo']
autos = ['Chevy', 'Tsuru']

combinados = zip(numeros, colores, autos)

for elemento in combinados:
    print(elemento)