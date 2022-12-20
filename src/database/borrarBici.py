import requests
import os
import json


def deleteOne(url, apiKey):
    assert isinstance(url, str)
    assert isinstance(apiKey, str)

    iD = input("Escriba aqui la id de la bici correspondiente para eliminarla: ")

    payload = json.dumps({
        "collection": "BICIS",
        "database": "BIBIKES",
        "dataSource": "Trabajo",
        "filter": {
            "_id": {"$oid": iD}
        }
    })

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': apiKey
    }

    print("Bicicleta eliminada correctamente")
    response = requests.request("POST", url, headers=headers, data=payload)


if __name__ == "__main__":
    url = os.environ["URLD"]
    apiKey = os.environ["API"]

    deleteOne(url, apiKey)
