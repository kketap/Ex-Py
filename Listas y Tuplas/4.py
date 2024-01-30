numeros = []

for i in range(6):
    numeros.append(int(input("Ingresa un numero ganador: ")))
numeros.sort()
print("Los numeros ganadores son: "+str(numeros))