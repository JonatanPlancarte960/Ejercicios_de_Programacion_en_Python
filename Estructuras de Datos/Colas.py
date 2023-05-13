# Colas
# Una cola se basa en el principio de el primero que llega es el primero que sale
# FIFO: First In - First Out

# Esto es una estructura de datos en Python que implementa una cola
from collections import deque # Modulo

alumnos = deque(["Sofía", "Mateo", "Valentina", "Alejandro", "Camila", "Sebastián", "Isabella", "Lucas", "Gabriela", "Daniel"])
print(alumnos)

alumnos.append("Krisprkas")
alumnos.append("Johnny")

print(alumnos)

alumnos.popleft() # Quita al ultimo pero de derecha a izquierda
print(alumnos)

alumnos.popleft()
print(alumnos)

alumnos.popleft()
print(alumnos)

print("-----------------------------------------")

cola1 = []

cola1.append("Gato")
cola1.append("Puppy")
cola1.append("Manchas")

print(cola1)

cola1.pop(0)
print(cola1)

cola1.pop(0)
print(cola1)