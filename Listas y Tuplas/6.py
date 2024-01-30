asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje"]

for i in range(len(asignaturas)-1, -1, -1):
    nota = float(input("Ingresa tu nota para {}: ".format(asignaturas[i])))
    if nota >= 4:
        asignaturas.pop(i)

print("Tienes que repetir: " + str(asignaturas))
        