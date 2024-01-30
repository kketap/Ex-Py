morse = {'A': '.-',     'B': '-...',   'C': '-.-.', 
         'D': '-..',    'E': '.',      'F': '..-.',
         'G': '--.',    'H': '....',   'I': '..',
         'J': '.---',   'K': '-.-',    'L': '.-..',
         'M': '--',     'N': '-.',     'O': '---',
         'P': '.--.',   'Q': '--.-',   'R': '.-.',
         'S': '...',    'T': '-',      'U': '..-',
         'V': '...-',   'W': '.--',    'X': '-..-',
         'Y': '-.--',   'Z': '--..'}

def codificarPalabra(palabra):

    palabraCodificada = ' '

    for i in palabra:
        
        palabraCodificada += morse.get(i.upper() , i) + ';'
    
    return palabraCodificada

def decodificadorPalabra(palabra):
    
    morseInvertido = {value:key for key , value in morse.items()}

    palabraDecodificada = ''
    
    for i in palabra.split(';'):

        palabraDecodificada += morseInvertido.get(i , i)

    return palabraDecodificada

def codificadorMensaje(mensaje):
    
    mensajeCodificado = ' '

    mensaje = mensaje.split()

    palabrasCodificadas = list(map(codificarPalabra , mensaje))

    return mensajeCodificado.join(palabrasCodificadas)

def decodificadorMensaje(mensaje):
    
    mensajeDecodificado = ' '

    mensaje = mensaje.split()

    palabrasDecoodificadas = list(map(decodificadorPalabra , mensaje))

    return mensajeDecodificado.join(palabrasDecoodificadas)

print(codificarPalabra('Python')) #Debe devolver '.--.;-.--;-;....;---;-.;'
print(decodificadorPalabra('.--.;-.--;-;....;---;-.')) #Debe devolver 'PYTHON'
print(codificadorMensaje('Hola Python')) #Debe devolver '....;---;.-..;.-; .--.;-.--;-;....;---;-.'
print(decodificadorMensaje('....;---;.-..;.- .--.;-.--;-;....;---;-.')) #Debe devolver 'HOLA PYTHON' 