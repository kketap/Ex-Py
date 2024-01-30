numero = int(input("Ingresa un numero entero: "))

for i in range(1,numero + 1, 2):
    for j in range(i,0,-2):
        print(j,end=" ")
    print("")