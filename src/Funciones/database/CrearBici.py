import os
import json
import requests


def crearBici(url, apiKey):
    assert isinstance(url, str)
    assert isinstance(apiKey, str)

    nombre = input("Nombre: ")
    tipo = input("Tipo: ")
    localizacion = input("Localizacion: ")
    material = input("Material: ")
    talla = input("Talla: ")
    cuadro = input("Cuadro: ")
    suspension = input("Suspension: ")
    tamaño_ruedas = input("Tamaño ruedas: ")
    velocidades = input("Velocidades: ")
    marca = input("Marca: ")
    imagen = str(input("Imagen: "))
    precio = input("Precio: ")  # Con simbolo de €
    iD = int(input("id: "))

    payload = json.dumps({
        "collection": "BICIS",
        "database": "BIBIKES",
        "dataSource": "Trabajo",
        "document": {
            "Nombre": nombre,
            "Tipo": tipo,
            "Localizacion": localizacion,
            "Caracteristicas": {
                "Material": material,
                "Talla": talla,
                "Cuadro": cuadro,
                "Suspension": suspension,
                "Tamaño ruedas": tamaño_ruedas,
                "Velocidades": velocidades,
                "Marca": marca
            },
            "Imagen": imagen,
            "Precio": precio,
            "id": iD
        }
    })

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': apiKey
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("Nueva bicicleta creada: " + response.text)


if __name__ == "__main__":
    url = os.environ["URLC"]
    apiKey = os.environ["API"]
    crearBici(url, apiKey)
