clientes = {}

opcion = 0

opcion = input("Ingresa una opcion del 1 al 6")

while opcion != 6:
    if opcion == 1:
        rut = input("Ingresa tu rut: ")
        nombre = input("Ingresa tu nombre: ")
        direccion = input("Ingresa tu direccion: ")
        telefono = input("Ingresa tu telefono: ")
        email = input("Ingresa tu email: ")
        vip = input("Ingresa si eres vip o no: ")
        cliente = {'nombre':nombre,'direccion':direccion,'telefono':telefono,'email':email,'vip':vip}
        clientes[rut] = cliente
        print(clientes)
    if opcion == 2:
        rut = input("Introduce el rut del cliente: ")
        if rut in clientes:
            del clientes[rut]
        else :
            print(rut," no existe")
            
    if opcion == 3:
        rut = input("Introduce el rut del cliente: ")
        if rut in clientes:
            print("Rut del cliente: ",rut)
            for clave,valor in clientes[rut].items():
                print(clave + ':', valor)
        else:
            print("No existe el cliente")
    if opcion == 4:
        print("Lista de clientes")
        for clave. valor in clientes.items():
            print(clave,valor['nombre'])
    if opcion == 5:
        print("Lista de clientes preferentes")
        for clave, valor in clientes.items():
            if valor['preferentes']:
                print(clave , valor['nombre'])
    else :
        print("Gracias por usar el servicio")
        break

opcion = input("Ingresa una opcion del 1 al 6")