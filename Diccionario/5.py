curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

totalCreditos = 0

for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'créditos')
    totalCreditos += creditos

print('Número total de créditos del curso: ', totalCreditos)