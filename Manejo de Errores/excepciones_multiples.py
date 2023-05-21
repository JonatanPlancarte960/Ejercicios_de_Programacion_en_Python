# Gestion de multiples excepciones

def funcion():
    raise ExceptionGroup("Grupo 1", [OSError(1), SystemError(2), ExceptionGroup("Grupo 2", [OSError(3), RecursionError(4)])])

try:
    funcion()
except* OSError as error:
    print("Hay OSError")
except* SystemError as error:
    print("Hay SystemError")
except* RecursionError as error:
    print("Hay RecursionError")

# Notas en las excepciones

try:
    raise TypeError("Mal tipo de dato")
except Exception as error:
    error.add_note("Es que pusiste entero en vez de flotante")
    error.add_note("Te equivocaste")
    error.add_note("Hola")
    print(error)

def funcion1():
    raise OSError("Operacion fallida")

problemas = []

for i in range(3):
    try:
        funcion()
    except Exception as error:
        error.add_note(f"Ocurrio en la iteracion {i+1}")
        problemas.append(error)

raise ExceptionGroup("Tenemos problemas", problemas)