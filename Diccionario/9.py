facturas = {}

cobrado = 0
pendiente = 0

mas = ''

while mas != 'T':
    if mas == 'A':
        clave = input("Introduce el numero de facturas: ")
        coste = float(input("Introduce el valor de la facturas: "))
        facturas[clave] = coste
        pendiente += coste
    if mas == 'P':
        clave = input("Introduce el numero de factura: ")
        coste = facturas.pop(clave,0)
        cobrado += coste
        pendiente -= coste
    print("Recaudado: ",cobrado)
    print("Pendiente de cobro: ",pendiente)
    mas = input("Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?: ")