import os
import json
import requests


def FindOne(url, ApiKey):
    assert isinstance(url, str)
    assert isinstance(ApiKey, str)

    ID = int(input("Encuentre la bicicleta que quiera. Inserte su id: "))

    payload = json.dumps({
        "collection": "BICIS",
        "database": "BIBIKES",
        "dataSource": "Trabajo",
        "filter": {"id": ID},
        "projection": {"_id": 0}
    }
    )

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': ApiKey
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.text == """{"document":null}""":
        print("Bici no existente")
    else:
        print("Bici con id encontrada, estos son sus datos: " + response.text)


if __name__ == "__main__":
    url = os.environ["URLR"]
    ApiKey = os.environ["API"]
    FindOne(url, ApiKey)
