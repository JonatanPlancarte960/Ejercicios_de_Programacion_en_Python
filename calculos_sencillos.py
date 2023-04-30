# Precedencia o Jerarquia de Operaciones
print("--------------- Precedencia o Jerarquia de Operaciones ---------------")
''' 
1.  Parentesis - Corchetes
2. Potencias - Raiz Cuadrada
3. Multiplicacion - Division
4. Suma - Resta
'''
print(2 + 2)
print((50 - 5 * 9) / 4)
impuesto = 16 / 100 # 16%
precio = 31149.30 # Precio de Laptop
print(precio * impuesto)

# Ejemplo de Operador Ternario
print("--------------- Ejemplo de Operador Ternario ---------------")
esta_dormido = False
status = "Esta dormido" if esta_dormido else "No esta dormido"
print(status)

# Cadenas de Caracteres
print("--------------- Cadenas de Caracteres ---------------")
print('''They've said "I'm Crazy"''') # They've said "I'm Crazy"
print('They\'ve said "I\'m Crazy"') # They've said "I'm Crazy"

print("Hola \n Mundo") # \n Salto de Linea
print("Hola \t Mundo") # Tabulador - Tab
print('C:\algun\nombre')
print('C:\\algun\\nombre')
print(r'C:\algun\nombre')

print("""
Hola soy Jonatan
    -h          Obten ayuda de la aplicacion
    -h url      Hackea a la url dada
""")

print(3 * 'o' + 'x')
print(2* 'xo')
print(100* 'xo')

print('Py' 'thon')
print('Py', 'thon') # Aqui pone un espacio

# Texto muy largo en print
print("En la pradera de los unicornios de la galaxia de las estrellas brillantes, se podía ver un arcoíris gigante que emanaba dulces aromas de fresas y rosas. " 
    "Los conejos voladores saltaban de nube en nube, mientras que los árboles caminaban con raíces de fuego y hojas de metal. " 
    "El sol brillaba con destellos de purpurina y la luna se movía al ritmo de una canción desconocida. ")

palabra = "Pythonista" # Esto tambien puede funcionar como una lista
print(palabra[0]) # Siempre me va a dar el primer elemento
print(palabra[5])
print(palabra[-1]) # Siempre me va a dar el ultimo elemento
print(palabra[-2])
print(palabra[-6])

# Obtener los dos primeros caracteres
print(palabra[0] + palabra[1]) # Concatenar dos elementos
print(palabra[0:2]) # Dame la posicion 0 hasta la posicion 2 excluyendola
print(palabra[2:5]) # Dame la posicion 2 a la 5 excluyendola
print(palabra[1:]) # Dame todos los elementos menos el 0
print(palabra[:]) # Dame todos los elementos

print(len(palabra))

print(palabra[0] + palabra[-1])

print(palabra[0:2+1]) # 0:3