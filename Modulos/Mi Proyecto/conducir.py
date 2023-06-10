# Este es el sistema de validacion de edad para expedicion de licencias bajo la ley de la CDMX

def conducir(edad = 0):
    if edad < 15 or edad > 80:
        return False
    elif edad >= 15 and edad < 18:
        return True, "Licencia Provisional"
    elif edad >= 18 and edad < 80:
        return True, "Licencia Normal"
    else:
        return False
    
def tipo_licencia(tipo_vehiculo = "automovil"):
    match tipo_vehiculo:
        case "automovil":
            return "Tipo A"
        case "motocicleta":
            return "Tipo A1"
        case "taxi":
            return "Tipo B"
        case _:
            return False