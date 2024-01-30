frase = input("Ingresa una frase: ")
vocals = ['a', 'e', 'i', 'o', 'u']

for vocal in vocals:
    times = 0
    for letter in frase:
        if letter == vocal:
            times += 1
    print("La vocal "+vocal+" aparece "+ str(times)+ " veces") 
