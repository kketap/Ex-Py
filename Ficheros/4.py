def contar_palabras(url):
    from urllib import request
    from urllib.error import URLError
    try :
        f = request.urlopen(url)
    except URLError:
        return('La url ' + url + 'no existe')
    else:
        contenido = f.read()
        return len(contenido.split())

print(contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(contar_palabras('https://no-existe.txt'))