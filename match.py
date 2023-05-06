# Estructura match, es como el swhitch case de otros lenguajes
# Evalua una variable y da el resultado y se detiene cuando encuentra una coincidencia

status = 404 # Not found

match status:
    case 400:
        print("Bad request") # Peticion incorrecta
    case 401 | 403 | 405:
        print("Client Error") # Prohibido
    case 404:
        print("Not found") # No encontrado
    case 418:
        print("I'm a teapot") # Soy una tetera
    case _:
        print("Error") # Este es el default o lo que ejecuta cuando las condiciones no se cumplen