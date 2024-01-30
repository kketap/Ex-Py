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
    return list(map(curso , notas))

print(aplicar_notas([1.0 , 3.2 , 4.5 , 5.5 , 6.4 , 6.9]))