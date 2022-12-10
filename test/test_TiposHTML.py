import os
import pytest

# Para probar otros tipos, cambiar en format tipos.
rutaTiposHTML = ".\\docs\\{tipos}.html".format(tipos="Montaña")
rutaTiposHTML = os.path.relpath(rutaTiposHTML)


def test_comprobarRutaTiposHTML():
    assert os.path.exists(rutaTiposHTML) == True


def test_comprobarArchivoTiposHMTL():
    assert os.path.isfile(rutaTiposHTML) == True
