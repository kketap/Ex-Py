def long_palabras(frase):
    palabras = frase.split()
    longitud = map(len , palabras)
    return dict(zip(palabras , longitud))
print(long_palabras("Bienvenido a Python"))

