import os
import pytest

# Para probar otros tipos, cambiar en format tipos.
rutaTiposHTML = ".\\docs\\{tipos}.html".format(tipos="Montaña")
rutaTiposHTML = os.path.relpath(rutaTiposHTML)


@pytest.mark.rutaTipoHTML
def test_comprobarRutaTiposHTML():
    assert os.path.exists(rutaTiposHTML) == True


@pytest.mark.ArchivoTipoHTML
def test_comprobarArchivoTiposHMTL():
    assert os.path.isfile(rutaTiposHTML) == True
