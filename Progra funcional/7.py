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
    
def aplicar_notas(notas):
    return {subject.upper():curso(nota) for subject , nota in notas.items()}

print(
aplicar_notas({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':2.4, 'Historia':4.6, 'Programación':6.9}))