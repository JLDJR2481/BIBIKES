import os
import pytest

# Para comprobar otras marcas, cambiar Marca en format
rutaMarcaHTML = ".\\docs\\{Marca}.html".format(Marca = "Riverside")
rutaMarcaHTML = os.path.relpath(rutaMarcaHTML)

@pytest.mark.rutaMarcaHTML
def test_comprobarRutaMarcaHTML():
    assert os.path.exists(rutaMarcaHTML)


@pytest.mark.ArchivoMarcaHTML
def test_comprobarArchivoMarcaHTML():
    assert os.path.exists(rutaMarcaHTML)