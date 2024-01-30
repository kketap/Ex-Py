def parsear_pib(url):
    from urllib import request
    from urllib.error import URLError

    try:
        with request.urlopen(url) as f:
            datos = f.read().decode('utf.8').split('\n')
    except URLError:
        return('La url no existe')
    else:
        años = datos.pop(0).split('\t')[1:]
        dict_pibs = {}
        for pais in datos:
            datos_pais = pais.split('\t')
            codigo_pais = datos_pais.pop(0)[-2:]
            dict_pais = {}
            for i in range(len(datos_pais)):
                dict_pais[años[i].strip()] = datos_pais[i].strip()

            dict_pais[codigo_pais] = dict_pais
        return dict_pibs
def pib(pibs , pais = 'ES'):
    print("AÑO\tPIB")
    for i , j in pibs[pais].items():
        print(i , '\t' , j)

pais = input('Introduce el codigo de un pais: ')
print('PIB per capita de ',pais)
pib(parsear_pib("https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"), pais)