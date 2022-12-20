import requests
import json
import os

# Funcion para crear un archivo JSON de la base de datos


def crearArchivoJSON(url, apiKey):
    assert isinstance(url, str)
    assert isinstance(apiKey, str)

    payload = json.dumps({
        "collection": "BICIS",
        "database": "BIBIKES",
        "dataSource": "Trabajo",
        "projection": {
            "_id": 0
        }
    })

    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': apiKey
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        result = (response.text)
        result = json.loads(result)

    except requests.exceptions.Timeout:
        print("Error: Timeout")
        SystemExit

    except requests.exceptions.ConnectionError:
        print("Ha ocurrido un error de Conexión")
        SystemExit

    else:
        f = open("docs/Bicis.json", "w", encoding="UTF-8")
        json.dump(result["documents"], f, ensure_ascii=False)
        f.close()
        print("Archivo JSON creado")
