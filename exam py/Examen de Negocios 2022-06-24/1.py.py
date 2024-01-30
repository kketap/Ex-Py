def vf(capital , tipo , periodo):
    for i in range(periodo):
        print("Año",i,":",capital * (1 + tipo / 100) ** (i + 1))
    return

def va(capital , tipo , periodo):
    for i in range(periodo):
        print("Año",-i,":",capital / (1 + tipo / 100) ** (i + 1))
    return

cantidad = float(input("Ingresa una cantidad: "))
tipo = float(input("Ingresa un tipo: "))
años = int(input("Ingresa los años: "))
print("Valor Futuro")
vf(cantidad , tipo , años)
print("Valor Actual")
va(cantidad , tipo , años)