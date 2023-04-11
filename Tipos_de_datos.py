# Tipos de datos
dato = "5" # Una cadena de caracteres o cadena de texto
print(dato + dato)
dato = 5 # Numerico - Entero
print(dato + dato)
dato = 5.0 # Numerico - Flotante
print(dato + dato)
dato = True # Booleano - Verdadero o Falso - True or False
print(dato + dato)
cinco = "5"
numero = 5
# print(cinco + numero)
"""
Error de sintaxis
Error en tiempo de ejecucion
Error de logica
Error o excepcion
"""
# Solucion 1: Convertir el valor
print(cinco + str(numero)) # int - string
print(int(cinco) + numero) # string - int
print(float(cinco) + numero) # string - float

# Solucion 2: Formato de cadenas
nombre = "Jonatan"
edad = 19
# El objetivo es imprimir: Hola, mi nombre es Jonatan y tengo 19 años
print("Hola, mi nombre es {} y tengo {} años".format(nombre, edad))

# Solucion 3: f-string
print(f"Hola, mi nombre es {nombre} y tengo {edad} años")
