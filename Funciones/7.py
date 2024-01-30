def func(listar):
    lista = []
    for i in listar:
        lista.append(i**2)
    return lista
print(func([1, 2, 3, 4, 5]))
print(func([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
