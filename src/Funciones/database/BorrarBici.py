import requests
import os
import json


def DeleteOne(url, ApiKey):
    assert isinstance(url, str)
    assert isinstance(ApiKey, str)

    ID = input("Escriba aqui la id de la bici correspondiente para eliminarla: ")

    payload = json.dumps({
        "collection": "BICIS",
        "database": "BIBIKES",
        "dataSource": "Trabajo",
        "filter": {
            "_id": {"$oid": ID}
        }
    })

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': ApiKey
    }

    print("Bicicleta eliminada correctamente")
    response = requests.request("POST", url, headers=headers, data=payload)


if __name__ == "__main__":
    url = os.environ["URLD"]
    ApiKey = os.environ["API"]

    DeleteOne(url, ApiKey)
