def contarPalabras(frase):

    palabras = frase.strip().split()

    frecuencias = {palabra:palabras.count(palabra) for palabra in palabras}

    repetidas = [palabra for palabra , frecuencia in frecuencias.items() if frecuencia > 1]

    return frecuencias , repetidas

freq , rep = contarPalabras("Tres tristes tigres trigaban trigo en un trigal")

print("Frecuencia de palabras: " , freq)
print("Palabras repetidas: " , rep)