frutas = {'platano':1.35,'manzana':8.0,'pera':8.5,'naranja':7.0}

fruta = input("Ingresa la fruta que quieres: ").lower()

kilos = float(input("Ingresa los kilos de la fruta que deseas: "))

if fruta in frutas:
    print(kilos, 'kilos de', fruta, 'valen', frutas[fruta]*kilos, '€')
else :
    print("Error")