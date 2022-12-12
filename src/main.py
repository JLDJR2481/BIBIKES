import json
import os
from Funciones.database.database import *
from Funciones.Indice import PaginaIndice
from Funciones.BicisMontaña import PaginaMontaña
from Funciones.BicisCarretera import PaginaCarretera
from Funciones.BicisCiudad import PaginaCiudad
from Funciones.BicisIndividuales import BicisIndividuales
from Funciones.BicisMarcas import *

# Definimos función para transformar el archivo JSON en un diccionario Python


def traerJSON():
    with open("docs/Bicis.json", encoding="UTF-8") as json_file:
        data = json.load(json_file)
    return data


if __name__ == "__main__":

 # Creamos un archivo JSON. Proceso más tardío
    url = os.environ["URL1"]
    ApiKey = os.environ["API"]
    crearArchivoJSON(url, ApiKey)

    # Utilizamos la funcion traerJSON para llamar al diccionario json transformado como variable datos
    datos = traerJSON()

# Empezamos a crear los htmls:
    # Indice
    PaginaIndice()

    # Bicis por marcas disponibles
    MarcaRiverside(datos)
    MarcaCERES(datos)
    MarcaBTWIN(datos)
    MarcaRockrider(datos)
    MarcaVanRysel(datos)
    MarcaElops(datos)
    MarcaTriban(datos)
    MarcaMOMA(datos)
    MarcaNTT(datos)

    # Bicis de Montaña
    PaginaMontaña(datos)

    # Bicis de Carretera
    PaginaCarretera(datos)

    # Bicis de Ciudad
    PaginaCiudad(datos)

    # Datos de bicis de forma individual
    BicisIndividuales(datos)
