def curso(nota):
    if nota < 4:
        return "Repitiendo"
    elif nota < 5:
        return "Salvando"
    elif nota < 6 :
        return "Bueno"
    elif nota < 7 :
        return "Muy Bueno"
    else :
        return "Todo mal"
    
def aprobados(subject):
    return (subject[1]>= 4)

def aplicar_notas(notas):
    aprobado = dict(filter(aprobados, notas.items()))
    subjects = map(str.upper , aprobado.keys())
    cursos = map(curso , aprobado.values())
    return dict(zip(subjects , cursos))

print(
aplicar_notas({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':2.0, 'Historia':4.6, 'Programación':6.9}))