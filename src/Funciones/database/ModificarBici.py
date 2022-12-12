import os
import requests
import json


def UpdateOne(url, ApiKey):
    assert isinstance(url, str)
    assert isinstance(ApiKey, str)

    ID = int(
        input("Indica la id correspondiente de la bicicleta para cambiar sus valores: "))
    Field = input("¿Qué dato quieres cambiar? Especifícalo aquí: ")
    Valor = input("¿Por cuál valor lo quieres cambiar?: ")

    payload = json.dumps({
        "collection": "BICIS",
        "database": "BIBIKES",
        "dataSource": "Trabajo",
        "filter": {"id": ID},
        "update": {"$set": {Field: Valor},
                   "projection": {"_id": 0}}
    })

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': ApiKey
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("Bicicleta modificada")


if __name__ == "__main__":
    url = os.environ["URLU"]
    ApiKey = os.environ["API"]
    UpdateOne(url, ApiKey)
