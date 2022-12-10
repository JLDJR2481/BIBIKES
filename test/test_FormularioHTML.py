import os
import pytest

rutaFormularioHTML = ".\\docs\\formulario.html"
rutaFormularioHTML = os.path.relpath(rutaFormularioHTML)


@pytest.mark.rutaFormularioHTML
def test_comprobarRutaFormularioHTML():
    assert os.path.exists(rutaFormularioHTML) != False


@pytest.mark.ArchivoFormularioHTML
def test_comprobarArchivoFormularioHTML():
    assert os.path.isfile(rutaFormularioHTML) == True
