texto = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres." 

frecuencias = {}

for i in texto.replace(" ",""):
    if i in frecuencias:
        frecuencias[i] += 1
    else :
        frecuencias[i] = 1

print(frecuencias)

frecMax = max(frecuencias.values())

posMax = list(frecuencias.values()).index(frecMax)

caracterMax = list(frecuencias.keys())[posMax]

print("Carácter más repetido: ",caracterMax)
palabras = {}

texto = texto.split(" ")

for i in texto:
    if caracterMax in i and not i in palabras:
        freq = 0
        for j in i:
            if j == caracterMax:
                freq += 1
        palabras[i] = freq

print(palabras)