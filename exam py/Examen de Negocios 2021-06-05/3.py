while True:
    operacion = input("Introduce la operación con el formato operando1 operador operando2: ")

    if operacion.lower() == "salir":
        break
    
    operacion = operacion.split()

    if len(operacion) != 3:
        print("Operación no válida. Se necesitan tres argumentos separados por espacio")
    
    else :
        a = float(operacion[0])
        operador = operacion[1]
        b = float(operacion[2])

        if operador == "+":
            print(a , operador , b , '=' , a + b)
        
        elif operador == "-":
            print(a, operador, b, '=', a - b)
        
        elif operador == "*":
            print(a, operador, b, '=', a * b)
        
        elif operador == "/":
            print(a, operador, b, '=', a / b)
        
        elif operador == "**":
            print(a, operador, b, '=', a ** b) 
        
        else :
            print("Operador no válido. Introduce uno de los siguientes operadores: + (suma), - (resta), * (producto), / (cociente), ** (potencia).")
          