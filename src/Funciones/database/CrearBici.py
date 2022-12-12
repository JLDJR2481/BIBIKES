import os
import json
import requests


def CrearBici(url, ApiKey):
    assert isinstance(url, str)
    assert isinstance(ApiKey, str)

    Nombre = input("Nombre: ")
    Tipo = input("Tipo: ")
    Localizacion = input("Localizacion: ")
    Material = input("Material: ")
    Talla = input("Talla: ")
    Cuadro = input("Cuadro: ")
    Suspension = input("Suspension: ")
    Tamaño_ruedas = input("Tamaño ruedas: ")
    Velocidades = input("Velocidades: ")
    Marca = input("Marca: ")
    Imagen = str(input("Imagen: "))
    Precio = input("Precio: ")  # Con simbolo de €
    ID = int(input("id: "))

    payload = json.dumps({
        "collection": "BICIS",
        "database": "BIBIKES",
        "dataSource": "Trabajo",
        "document": {
            "Nombre": Nombre,
            "Tipo": Tipo,
            "Localizacion": Localizacion,
            "Caracteristicas": {
                "Material": Material,
                "Talla": Talla,
                "Cuadro": Cuadro,
                "Suspension": Suspension,
                "Tamaño ruedas": Tamaño_ruedas,
                "Velocidades": Velocidades,
                "Marca": Marca
            },
            "Imagen": Imagen,
            "Precio": Precio,
            "id": ID
        }
    })

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': ApiKey
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("Nueva bicicleta creada: " + response.text)


if __name__ == "__main__":
    url = os.environ["URLC"]
    ApiKey = os.environ["API"]
    CrearBici(url, ApiKey)
