monedas = [500 , 100 , 50]

cambio = [0 , 0 ,0]

cantidad = int(input("Ingresa una cantidad entera: "))

print("Para sumar", cantidad , ", se necesitan " , end='')

for i in  range(len(monedas)):
    while cantidad >= monedas[i]:
        cantidad -= monedas[i]
        cambio[i] += 1

print(sum(cambio) , 'monedas: ')

for i in range(len(monedas)):
    print(cambio[i] , 'monedas de ' , monedas[i] , '$')