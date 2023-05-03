tu_dinero = int(input("¿Cuanto dinero traes? "))
edad = int(input("¿Cual es tu edad? "))

cover = 100
costo_vip = 500
print("Edad: ", edad)
print("Tu dinero: ", tu_dinero)

if edad >= 18 and  tu_dinero >= cover:
    print("Cobro de Cover: ", cover)
    tu_dinero = tu_dinero - cover
    print("Tu dinero: ", tu_dinero)
    print("Puedes pasar")
    vip = int(input("¿Quieres pasar al VIP?\n1: Si\n2: No\nRespuesta: "))
    if vip == 1 and tu_dinero >= costo_vip:
        print("Cobro de VIP: ", costo_vip)
        tu_dinero = tu_dinero - costo_vip
        print("Tu dinero: ", tu_dinero)
        print("Pasale al VIP")
    elif vip == 1 and tu_dinero < costo_vip:
        
        print("No puedes pasar al VIP, cuesta 500")
        print("Tu dinero: ", tu_dinero)
    elif vip == 2:
        print("No se preocupe, siga disfrutando")
        print("Tu dinero: ", tu_dinero)
elif edad < 18:
    print("Debes tener mas edad para entrar")
else:
    print("No te alcanza")