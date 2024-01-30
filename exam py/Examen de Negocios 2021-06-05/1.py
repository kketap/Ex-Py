tupla = (5, 20, 3, 7, 6, 8)

k = int(input("Cuantos minimos y maximos quieres?: "))

lista = list(tupla)

if len(lista) < 2 * k:
    print('No se pueden extraer', k, 'máximos y mínimos de la tupla porque solo cotinene', len(lista), 'elementos.')
else :
    lista.sort()

    tupla2 = tuple(lista[:k] + lista[-k:])

    print(tupla2)