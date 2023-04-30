tu_dinero = int(input("¿Cuanto traes? "))
edad = 18
cover = 100
costo_vip = 500
print("Edad: ", edad)
print("Tu dinero: ", tu_dinero)

if edad >= 18 and  tu_dinero >= cover:
    print("Cobro de Cover: ", cover)
    tu_dinero = tu_dinero - cover
    print("Tu dinero: ", tu_dinero)
    print("Puedes pasar")
    if tu_dinero >= costo_vip:
        print("Cobro de VIP: ", costo_vip)
        tu_dinero = tu_dinero - costo_vip
        print("Tu dinero: ", tu_dinero)
        print("Pasale al VIP")
    else:
        print("No puedes pasar al VIP, cuesta 500")