numeros = [50, 4, 28, 33, 12]

suma = 0

print("SUMAR Y GANAR")
print("Vaya sumando todos los números que le iré diciendo. Empezamos por 0.")

for i in range(len(numeros)):
    respuesta = int(input("Más " + str(numeros[i]) + ": "))
    suma += numeros[i]
    
    if respuesta != suma:
        print("Te has equivocado, pero has acertado", i, "veces seguidas.")
        break

if suma == sum(numeros):
    print("Enhorabuena")