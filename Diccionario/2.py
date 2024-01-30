nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
direccion = input("Ingresa tu dirección: ")
telefono = input("Ingresa tu N° de celular: ")

persona = {'Nombre':nombre,'Edad':edad,'Dirección':direccion,'Telefono':telefono}

print(persona['Nombre'], 'tiene', persona['Edad'], 'años, vive en', persona['Dirección'], 'y su número de teléfono es', persona['Telefono'])