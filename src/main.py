import json
import os
from funciones.database.database import crearArchivoJSON
from funciones.indice import paginaIndice
from funciones.bicisMontaña import paginaMontaña
from funciones.bicisCarretera import paginaCarretera
from funciones.bicisCiudad import paginaCiudad
from funciones.bicisIndividuales import bicisIndividuales
from funciones.bicisMarcas import *

# Definimos función para transformar el archivo JSON en un diccionario Python


def traerJSON():
    with open("docs/Bicis.json", encoding="UTF-8") as json_file:
        data = json.load(json_file)
    return data


if __name__ == "__main__":

 # Creamos un archivo JSON. Proceso más tardío
    url = os.environ["URL1"]
    apiKey = os.environ["API"]
    crearArchivoJSON(url, apiKey)

    # Utilizamos la funcion traerJSON para llamar al diccionario json transformado como variable datos
    datos = traerJSON()

# Empezamos a crear los htmls:
    # Indice
    paginaIndice()

    # Bicis por marcas disponibles
    marcaRiverside(datos)
    marcaCERES(datos)
    marcaBTWIN(datos)
    marcaRockrider(datos)
    marcaVanRysel(datos)
    marcaElops(datos)
    marcaTriban(datos)
    marcaMOMA(datos)
    marcaNTT(datos)

    # Bicis de Montaña
    paginaMontaña(datos)

    # Bicis de Carretera
    paginaCarretera(datos)

    # Bicis de Ciudad
    paginaCiudad(datos)

    # Datos de bicis de forma individual
    bicisIndividuales(datos)
