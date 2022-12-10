import os
import pytest

rutaJSON = ".\\docs\\Bicis.json"
rutaJSON = os.path.relpath(rutaJSON)


@pytest.mark.rutaJSON
def test_comprobarRutaArchivoJSON():
    assert os.path.exists(rutaJSON) != False


@pytest.mark.ArchivoJSON
def test_comprobarArchivoJSON():
    assert os.path.isfile(rutaJSON) == True
