# Operadores Aritmeticos

numero1 = 5
numero2 = 10

# Operador de suma / Concatenacion
print("--------------- Suma ---------------")
print(numero1 + numero2)
numero3 = "5"
numero4 = "10"
print(numero3 + numero4)

# Operador de resta
print("--------------- Resta ---------------")
print(numero1 - numero2)
print(numero2 - numero1)
# print(numero3 - numero4) # Esto no es posible

# Operador de multiplicacion
print("--------------- Multiplicacion ---------------")
print(numero1 * numero2)
# print(numero3 * numero4) # Esto no es posible

# Operador de division
print("--------------- Division ---------------")
print(numero1 / numero2)
print(numero2 / numero1)

# Operador modulo
print("--------------- Modulo ---------------")
# El operador modulo nos devuelve el residuo de una division entera
print(numero1 % numero2)
print(numero2 % numero1)

# Potencia de un numero
# N cantidad de veces un numero multiplicado por si mismo
print("--------------- Potencia ---------------")
print(numero1 ** numero2)
print(numero2 ** numero1)

# Division entera
# Hace la division pero el resultado es sin punto decimal
print("--------------- Division Entera ---------------")
print(numero1 // numero2)
print(numero2 // numero1)

# Operadores relacionales
# Mayor que
# Devuelve True si el numero de la izquierda es mayor que el numero de la derecha
print("--------------- Mayor Que ---------------")
print(numero1 > numero2)
print(numero2 > numero1)

# Menor Que
# Devuelve True si el numero de la izquierda es menor que el numero de la derecha
print("--------------- Menor Que ---------------")
print(numero1 < numero2)
print(numero2 < numero1)

# Operador de igualdad
print("--------------- Igualdad - Igual Que ---------------")
print(numero1 == numero2)
print(5 == 5)
print(5 == "5")
print(5 == 5.0) # Datos flotantes y enteros los trata como numericos

# Operador de desigualdad
# Nos da True si ambos valores no son iguales o son diferentes
print("--------------- Desigualdad ---------------")
print(numero1 != numero2)
print(numero1 != numero1)

# Operador mayor o igual que
print("--------------- Mayor o Igual Que ---------------")
# Nos da True si el valor de la izquierda es mayor o igual al de la derecha
print(numero1 >= numero2)
print(numero2 >= numero1)

# Operador menor o igual que
# Nos da True si el valor de la izquierda es menor o igual al de la derecha
print("--------------- Menor o Igual Que ---------------")
print(numero1 <= numero2)
print(numero2 <= numero1)

# Operadores bit a bit
a = 2 # Binario: 10
b = 3 # Binario: 11

# Operador AND Bit a Bit
# Si los dos son 1 devuelve 1, sino devuelve 0
print("--------------- AND Bit a Bit ---------------")
print(a & b)

# Operador OR Bit a Bit
# Si algunos de los dos son 1 devuelve 1, si ningununo de los dos es 1 duvuelve 0
print("--------------- OR Bit a Bit ---------------")
print(a | b)

# Operador XOR Bit a Bit
# Si ambos numeros son iguales devuelve 0, si son diferentes devuelve 1
print("--------------- XOR Bit a Bit ---------------")
print(a ^ b)

# Operador NOT Bit a Bit
# Invertir cada Bit en el operando
# Este es un operador de un solo numero
# Este operador saca el complemento del numero
# 00000010 = 2
# 11111101 = -2 "(-1)"
# -2 - 1 = -3
print("--------------- NOT Bit a Bit ---------------")
print(~a)
print(~b)

# Desplazamiento a la derecha
# Desplazar hacia la derecha los bits x cantidad de posiciones
# 00000010 = 2
# 00000011 = 3
print("--------------- Desplazamiento a la derecha ---------------")
print(a >> b) # 00000000 - 01 = 0
print(b >> a) # 00000000 - 11 = 0

# Dezplazamiento a la izquierda
# Desplazar hacia la izquierda los bits x cantidad de posiciones
# 00000010 = 2
# 00000011 = 3
print(a << b) # 00010000 = 16
print(b << a) # 00001100 = 12

# Operadores Logicos
# Los Operadores Logicos hacen operaciones con valores booleanos
print("--------------- Operadores Logicos ---------------")
print("--------------- Operador Logico AND ---------------")
# Devuelve True si todas las condiciones son Verdaderas (True)
costo_cigarros = 50
dinero = 100
edad = 20
print(dinero >= costo_cigarros and edad >= 18)
print(True and True)
print(True and False)
print(False and False)

print("--------------- Operador Logico OR ---------------")
# Devuelve True si al menos una de las condiciones es verdadera (True)
costo_cigarros = 50
dinero = 100
edad = 20
print(dinero >= costo_cigarros or edad >= 18)
print(True or True)
print(True or False)
print(False or False)

print("--------------- Operador Logico NOT ---------------")
# El Operador Logico NOT invierte el resultado de una condicion
costo_cigarros = 50
dinero = 100
edad = 20
print(not(dinero >= costo_cigarros or edad >= 18))
print(not(True or True))
print(not(True or False))
print(not(False or False))
print(not True)
print(not False)

# Operadores de Pertenencia
print("--------------- Operadores de Pertenencia ---------------")
# Un Operador de Pertenencia indica si algo pertenece a un conjunto de datos, a una lista, a "algo"
lista = [1, 2, 3, 4, 5]
print(lista)
print("--------------- Operador de Pertenencia IN ---------------")
# IN -> Pertenece a - Esta en
# Devuelve True si pertenece a una lista
print(3 in lista)
print(7 in lista)

print("--------------- Operador de Pertenencia NOT IN ---------------")
# not in -> No pertenece a - No esta en
# Devuelve True si no pertenece a una lista
print(3 not in lista)
print(7 not in lista)

# Operadores de Indentidad
print("--------------- Operadores de Identidad ---------------")
# Sirve para saber si algo esta en la misma ubicacion en memoria
print("--------------- Operador de Identidad IS ---------------")
# Devuelve True si algo se refiere al mismo objeto
a = 3
b = 3
c = 4
d = a
print(a is b)
print(a is d)
print(a is c)
print("--------------- Operador de Identidad IS NOT ---------------")
# Devuelve True si algo no se refiere al mismo objeto
print(a is not b)
print(a is not d)
print(a is not c)

a = 10
print(a)
print(d)