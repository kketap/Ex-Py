persona = {}

continuar = True

while continuar :
    clave = input("Ingresa los datos que quieres introducir: ")
    valor = input(clave + ':')
    persona[clave] = valor
    print(persona)
    continuar = input("Quieres añadir algun dato extra?: ") == "Si"