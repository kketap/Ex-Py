cesta = {}

continuar = True

while continuar :
    item = input("Ingresa los productos que desas: ")
    precio = float(input("Introduce el precio de "+item+" :"))
    cesta[item] = precio
    continuar = input("Deseas seguir comprando?: ") == "Si"
coste = 0
print("Lista de compra")
for item,precio in cesta.items():
    print(item, '\t', precio)
    coste += precio
print("Coste total: ",coste)
