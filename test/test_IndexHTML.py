import os
import pytest

rutaIndexHTML = ".\\docs\\index.html"
rutaIndexHTML = os.path.relpath(rutaIndexHTML)


@pytest.mark.rutaIndexHTML
def test_comprobarRutaIndexHTML():
    assert os.path.exists(rutaIndexHTML) != False


@pytest.mark.ArchivoIndexHTML
def test_comprobarArchivoIndexHTML():
    assert os.path.isfile(rutaIndexHTML) == True
