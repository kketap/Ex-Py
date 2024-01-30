def funcion_lista(funcion , lista):
    l = []
    for i in lista:
        l.append(funcion(i))
    return l
def cuadrado(n):
    return n * n
print(funcion_lista(cuadrado,[1,2,3,4]))