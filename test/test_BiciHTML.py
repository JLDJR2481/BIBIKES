import pytest
import os

# Para hacer mas pruebas, cambiar el integer ubicado en format
rutaBiciHTML = ".\\docs\\Bici{id}.html".format(id=1)
rutaBiciHTML = os.path.relpath(rutaBiciHTML)


@pytest.mark.rutaBiciHTML
def test_comprobarRutaBiciHTML():
    assert os.path.exists(rutaBiciHTML) == True


@pytest.mark.ArchivoBiciHTML
def test_comprobarArchivoBiciHTML():
    assert os.path.isfile(rutaBiciHTML) != False
