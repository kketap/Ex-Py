asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lenguaje"]
notas = []

for asignatura in asignaturas:
    nota = input("Ingrese la nota que has sacado en: "+asignatura+"?")
    notas.append(nota)
for i in range(len(asignaturas)):
    print("En ",asignaturas[i]," has sacado",notas[i])
