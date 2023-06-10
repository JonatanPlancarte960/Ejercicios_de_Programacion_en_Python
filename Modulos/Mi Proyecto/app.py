import conducir as cd

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        break
    except ValueError:
        print("Edad incorrecta, intenta de nuevo")

if cd.conducir(edad):
    print("Puedes conducir")
    vehiculo = input("Tipo de vehiculo que manejas: (automovil, motocicleta o taxi): ")
    tipo = cd.tipo_licencia(vehiculo)
    if tipo:
        print("Licencias", tipo)
    else:
        print("Ese tipo de vehiculo no existe")
else:
    print("No puedes conducir")