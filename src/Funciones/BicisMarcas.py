import json


def crearHTML(title, content):
    with open(title + ".html", "w", encoding="UTF-8") as f:
        f.write(content)
        print("Archivo HTML creado")


def marcaRiverside(datos):
    html = """
<!DOCTYPE html>
<html lang="ES" dir="ltr">
  <head>
    <link href="css/OtherPages.css" rel="stylesheet" type="text/css">
    <link rel="icon" href="Img/favicon.png">
    <title>BIBIKES - Marca - Riverside</title>
    <meta name="description" content="Pagina del catálogo de marcas disponibles">
    <meta charset="UTF-8">
    <meta name="author" content="Juan Pérez & José Luis De Jesús">
    <meta name="copyright" content="CIFP Francesc de Borja Moll">
    <meta name="generator" content="Visual Studio Code">
    <meta name="keywords" content="Bicis, Carretera, Montaña, Ciudad, Marcas">
    <base target="_blank">
  </head>

  <body class="body">
    <header
      style="
        background: url(Img/banner.jpg);
        background-size: cover;
        background-repeat: no-repeat;
      "
    >
      <!--Esto es el header-->
      <section class="cabecera">
        <br><br>
        <h1>BIBIKES</h1>
        <br><br>
      </section>
      <div class="content">
        <p>Todos los tipos de bicicletas disponibles bajo un mismo techo</p>
        <br><br>
      </div>
    </header>
    <!--Esto es el header-->
    <br>
    <div>
      <h2>Bicicletas disponibles</h2>
    </div>
    <br><br>
    <div id="flex-container">"""
    for i in datos:
        if i["Caracteristicas"]["Marca"] == "Riverside":
            html += """
      <section>
        <div class="prueba">
          <div class="caja">
            <p>{nombre}</p>
          </div>
          <div class="caja">
            <img
              class="FotoDeLaBici" src="{imagen}" alt = "Foto de la bici">
          </div>
          <div class="caja">
            <p><b>Localización: </b>{localizacion}</p>
          </div>
          <div class="caja">
            <p><b>Precio: </b>{precio}</p>
          </div>
          <div class="caja">
            <a href="Bici{id}.html">Más detalles</a>
          </div>
        </div>
      </section>""".format(nombre=i["Nombre"], imagen=i["Imagen"], localizacion=i["Localizacion"], precio=i["Precio"], id=i["id"])
    html += """
    </div>
  </body>
</html>"""
    crearHTML("docs/Riverside", html)


def marcaCERES(datos):
    html = """
<!DOCTYPE html>
<html lang="ES" dir="ltr">
  <head>
    <link href="css/OtherPages.css" rel="stylesheet" type="text/css">
    <link rel="icon" href="Img/favicon.png">
    <title>BIBIKES - Marca - CERES</title>
    <meta name="description" content="Pagina del catálogo de marcas disponibles">
    <meta charset="UTF-8">
    <meta name="author" content="Juan Pérez & José Luis De Jesús">
    <meta name="copyright" content="CIFP Francesc de Borja Moll">
    <meta name="generator" content="Visual Studio Code">
    <meta name="keywords" content="Bicis, Carretera, Montaña, Ciudad, Marcas">
    <base target="_blank">
  </head>

  <body class="body">
    <header
      style="
        background: url(Img/banner.jpg);
        background-size: cover;
        background-repeat: no-repeat;
      "
    >
      <!--Esto es el header-->
      <section class="cabecera">
        <br><br>
        <h1>BIBIKES</h1>
        <br><br>
      </section>
      <div class="content">
        <p>Todos los tipos de bicicletas disponibles bajo un mismo techo</p>
        <br><br>
      </div>
    </header>
    <!--Esto es el header-->
    <br>
    <div>
      <h2>Bicicletas disponibles</h2>
    </div>
    <br><br>
    <div id="flex-container">"""
    for i in datos:
        if i["Caracteristicas"]["Marca"] == "CERES":
            html += """
      <section>
        <div class="prueba">
          <div class="caja">
            <p>{nombre}</p>
          </div>
          <div class="caja">
            <img
              class="FotoDeLaBici" src="{imagen}" alt = "Foto de la bici">
          </div>
          <div class="caja">
            <p><b>Localización: </b>{localizacion}</p>
          </div>
          <div class="caja">
            <p><b>Precio: </b>{precio}</p>
          </div>
          <div class="caja">
            <a href="Bici{id}.html">Más detalles</a>
          </div>
        </div>
      </section>""".format(nombre=i["Nombre"], imagen=i["Imagen"], localizacion=i["Localizacion"], precio=i["Precio"], id=i["id"])
    html += """
    </div>
  </body>
</html>"""
    crearHTML("docs/CERES", html)


def marcaBTWIN(datos):
    html = """
<!DOCTYPE html>
<html lang="ES" dir="ltr">
  <head>
    <link href="css/OtherPages.css" rel="stylesheet" type="text/css">
    <link rel="icon" href="Img/favicon.png">
    <title>BIBIKES - Marca - BWTIN</title>
    <meta name="description" content="Pagina del catálogo de marcas disponibles">
    <meta charset="UTF-8">
    <meta name="author" content="Juan Pérez & José Luis De Jesús">
    <meta name="copyright" content="CIFP Francesc de Borja Moll">
    <meta name="generator" content="Visual Studio Code">
    <meta name="keywords" content="Bicis, Carretera, Montaña, Ciudad, Marcas">
    <base target="_blank">
  </head>

  <body class="body">
    <header
      style="
        background: url(Img/banner.jpg);
        background-size: cover;
        background-repeat: no-repeat;
      "
    >
      <!--Esto es el header-->
      <section class="cabecera">
        <br><br>
        <h1>BIBIKES</h1>
        <br><br>
      </section>
      <div class="content">
        <p>Todos los tipos de bicicletas disponibles bajo un mismo techo</p>
        <br><br>
      </div>
    </header>
    <!--Esto es el header-->
    <br>
    <div>
      <h2>Bicicletas disponibles</h2>
    </div>
    <br><br>
    <div id="flex-container">"""
    for i in datos:
        if i["Caracteristicas"]["Marca"] == "BTWIN":
            html += """
      <section>
        <div class="prueba">
          <div class="caja">
            <p>{nombre}</p>
          </div>
          <div class="caja">
            <img
              class="FotoDeLaBici" src="{imagen}" alt = "Foto de la bici">
          </div>
          <div class="caja">
            <p><b>Localización: </b>{localizacion}</p>
          </div>
          <div class="caja">
            <p><b>Precio: </b>{precio}</p>
          </div>
          <div class="caja">
            <a href="Bici{id}.html">Más detalles</a>
          </div>
        </div>
      </section>""".format(nombre=i["Nombre"], imagen=i["Imagen"], localizacion=i["Localizacion"], precio=i["Precio"], id=i["id"])
    html += """
    </div>
  </body>
</html>"""
    crearHTML("docs/BTWIN", html)


def marcaRockrider(datos):
    html = """
<!DOCTYPE html>
<html lang="ES" dir="ltr">
  <head>
    <link href="css/OtherPages.css" rel="stylesheet" type="text/css">
    <link rel="icon" href="Img/favicon.png">
    <title>BIBIKES - Marca - Rockrider</title>
    <meta name="description" content="Pagina del catálogo de marcas disponibles">
    <meta charset="UTF-8">
    <meta name="author" content="Juan Pérez & José Luis De Jesús">
    <meta name="copyright" content="CIFP Francesc de Borja Moll">
    <meta name="generator" content="Visual Studio Code">
    <meta name="keywords" content="Bicis, Carretera, Montaña, Ciudad, Marcas">
    <base target="_blank">
  </head>

  <body class="body">
    <header
      style="
        background: url(Img/banner.jpg);
        background-size: cover;
        background-repeat: no-repeat;
      "
    >
      <!--Esto es el header-->
      <section class="cabecera">
        <br><br>
        <h1>BIBIKES</h1>
        <br><br>
      </section>
      <div class="content">
        <p>Todos los tipos de bicicletas disponibles bajo un mismo techo</p>
        <br><br>
      </div>
    </header>
    <!--Esto es el header-->
    <br>
    <div>
      <h2>Bicicletas disponibles</h2>
    </div>
    <br><br>
    <div id="flex-container">"""
    for i in datos:
        if i["Caracteristicas"]["Marca"] == "Rockrider":
            html += """
      <section>
        <div class="prueba">
          <div class="caja">
            <p>{nombre}</p>
          </div>
          <div class="caja">
            <img
              class="FotoDeLaBici" src="{imagen}" alt = "Foto de la bici">
          </div>
          <div class="caja">
            <p><b>Localización: </b>{localizacion}</p>
          </div>
          <div class="caja">
            <p><b>Precio: </b>{precio}</p>
          </div>
          <div class="caja">
            <a href="Bici{id}.html">Más detalles</a>
          </div>
        </div>
      </section>""".format(nombre=i["Nombre"], imagen=i["Imagen"], localizacion=i["Localizacion"], precio=i["Precio"], id=i["id"])
    html += """
    </div>
  </body>
</html>"""
    crearHTML("docs/Rockrider", html)


def marcaVanRysel(datos):
    html = """
<!DOCTYPE html>
<html lang="ES" dir="ltr">
  <head>
    <link href="css/OtherPages.css" rel="stylesheet" type="text/css">
    <link rel="icon" href="Img/favicon.png">
    <title>BIBIKES - Marca - Van Rysel</title>
    <meta name="description" content="Pagina del catálogo de marcas disponibles">
    <meta charset="UTF-8">
    <meta name="author" content="Juan Pérez & José Luis De Jesús">
    <meta name="copyright" content="CIFP Francesc de Borja Moll">
    <meta name="generator" content="Visual Studio Code">
    <meta name="keywords" content="Bicis, Carretera, Montaña, Ciudad, Marcas">
    <base target="_blank">
  </head>

  <body class="body">
    <header
      style="
        background: url(Img/banner.jpg);
        background-size: cover;
        background-repeat: no-repeat;
      "
    >
      <!--Esto es el header-->
      <section class="cabecera">
        <br><br>
        <h1>BIBIKES</h1>
        <br><br>
      </section>
      <div class="content">
        <p>Todos los tipos de bicicletas disponibles bajo un mismo techo</p>
        <br><br>
      </div>
    </header>
    <!--Esto es el header-->
    <br>
    <div>
      <h2>Bicicletas disponibles</h2>
    </div>
    <br><br>
    <div id="flex-container">"""
    for i in datos:
        if i["Caracteristicas"]["Marca"] == "Van Rysel":
            html += """
      <section>
        <div class="prueba">
          <div class="caja">
            <p>{nombre}</p>
          </div>
          <div class="caja">
            <img
              class="FotoDeLaBici" src="{imagen}" alt = "Foto de la bici">
          </div>
          <div class="caja">
            <p><b>Localización: </b>{localizacion}</p>
          </div>
          <div class="caja">
            <p><b>Precio: </b>{precio}</p>
          </div>
          <div class="caja">
            <a href="Bici{id}.html">Más detalles</a>
          </div>
        </div>
      </section>""".format(nombre=i["Nombre"], imagen=i["Imagen"], localizacion=i["Localizacion"], precio=i["Precio"], id=i["id"])
    html += """
    </div>
  </body>
</html>"""
    crearHTML("docs/VanRysel", html)


def marcaElops(datos):
    html = """
<!DOCTYPE html>
<html lang="ES" dir="ltr">
  <head>
    <link href="css/OtherPages.css" rel="stylesheet" type="text/css">
    <link rel="icon" href="Img/favicon.png">
    <title>BIBIKES - Marca - Elops</title>
    <meta name="description" content="Pagina del catálogo de marcas disponibles">
    <meta charset="UTF-8">
    <meta name="author" content="Juan Pérez & José Luis De Jesús">
    <meta name="copyright" content="CIFP Francesc de Borja Moll">
    <meta name="generator" content="Visual Studio Code">
    <meta name="keywords" content="Bicis, Carretera, Montaña, Ciudad, Marcas">
    <base target="_blank">
  </head>

  <body class="body">
    <header
      style="
        background: url(Img/banner.jpg);
        background-size: cover;
        background-repeat: no-repeat;
      "
    >
      <!--Esto es el header-->
      <section class="cabecera">
        <br><br>
        <h1>BIBIKES</h1>
        <br><br>
      </section>
      <div class="content">
        <p>Todos los tipos de bicicletas disponibles bajo un mismo techo</p>
        <br><br>
      </div>
    </header>
    <!--Esto es el header-->
    <br>
    <div>
      <h2>Bicicletas disponibles</h2>
    </div>
    <br><br>
    <div id="flex-container">"""
    for i in datos:
        if i["Caracteristicas"]["Marca"] == "Elops":
            html += """
      <section>
        <div class="prueba">
          <div class="caja">
            <p>{nombre}</p>
          </div>
          <div class="caja">
            <img
              class="FotoDeLaBici" src="{imagen}" alt = "Foto de la bici">
          </div>
          <div class="caja">
            <p><b>Localización: </b>{localizacion}</p>
          </div>
          <div class="caja">
            <p><b>Precio: </b>{precio}</p>
          </div>
          <div class="caja">
            <a href="Bici{id}.html">Más detalles</a>
          </div>
        </div>
      </section>""".format(nombre=i["Nombre"], imagen=i["Imagen"], localizacion=i["Localizacion"], precio=i["Precio"], id=i["id"])
    html += """
    </div>
  </body>
</html>"""
    crearHTML("docs/Elops", html)


def marcaTriban(datos):
    html = """
<!DOCTYPE html>
<html lang="ES" dir="ltr">
  <head>
    <link href="css/OtherPages.css" rel="stylesheet" type="text/css">
    <link rel="icon" href="Img/favicon.png">
    <title>BIBIKES - Marca - Triban</title>
    <meta name="description" content="Pagina del catálogo de marcas disponibles">
    <meta charset="UTF-8">
    <meta name="author" content="Juan Pérez & José Luis De Jesús">
    <meta name="copyright" content="CIFP Francesc de Borja Moll">
    <meta name="generator" content="Visual Studio Code">
    <meta name="keywords" content="Bicis, Carretera, Montaña, Ciudad, Marcas">
    <base target="_blank">
  </head>

  <body class="body">
    <header
      style="
        background: url(Img/banner.jpg);
        background-size: cover;
        background-repeat: no-repeat;
      "
    >
      <!--Esto es el header-->
      <section class="cabecera">
        <br><br>
        <h1>BIBIKES</h1>
        <br><br>
      </section>
      <div class="content">
        <p>Todos los tipos de bicicletas disponibles bajo un mismo techo</p>
        <br><br>
      </div>
    </header>
    <!--Esto es el header-->
    <br>
    <div>
      <h2>Bicicletas disponibles</h2>
    </div>
    <br><br>
    <div id="flex-container">"""
    for i in datos:
        if i["Caracteristicas"]["Marca"] == "Triban":
            html += """
      <section>
        <div class="prueba">
          <div class="caja">
            <p>{nombre}</p>
          </div>
          <div class="caja">
            <img
              class="FotoDeLaBici" src="{imagen}" alt = "Foto de la bici">
          </div>
          <div class="caja">
            <p><b>Localización: </b>{localizacion}</p>
          </div>
          <div class="caja">
            <p><b>Precio: </b>{precio}</p>
          </div>
          <div class="caja">
            <a href="Bici{id}.html">Más detalles</a>
          </div>
        </div>
      </section>""".format(nombre=i["Nombre"], imagen=i["Imagen"], localizacion=i["Localizacion"], precio=i["Precio"], id=i["id"])
    html += """
    </div>
  </body>
</html>"""
    crearHTML("docs/Triban", html)


def marcaMOMA(datos):
    html = """
<!DOCTYPE html>
<html lang="ES" dir="ltr">
  <head>
    <link href="css/OtherPages.css" rel="stylesheet" type="text/css">
    <link rel="icon" href="Img/favicon.png">
    <title>BIBIKES - Marca - MOMA</title>
    <meta name="description" content="Pagina del catálogo de marcas disponibles">
    <meta charset="UTF-8">
    <meta name="author" content="Juan Pérez & José Luis De Jesús">
    <meta name="copyright" content="CIFP Francesc de Borja Moll">
    <meta name="generator" content="Visual Studio Code">
    <meta name="keywords" content="Bicis, Carretera, Montaña, Ciudad, Marcas">
    <base target="_blank">
  </head>

  <body class="body">
    <header
      style="
        background: url(Img/banner.jpg);
        background-size: cover;
        background-repeat: no-repeat;
      "
    >
      <!--Esto es el header-->
      <section class="cabecera">
        <br><br>
        <h1>BIBIKES</h1>
        <br><br>
      </section>
      <div class="content">
        <p>Todos los tipos de bicicletas disponibles bajo un mismo techo</p>
        <br><br>
      </div>
    </header>
    <!--Esto es el header-->
    <br>
    <div>
      <h2>Bicicletas disponibles</h2>
    </div>
    <br><br>
    <div id="flex-container">"""
    for i in datos:
        if i["Caracteristicas"]["Marca"] == "MOMA":
            html += """
      <section>
        <div class="prueba">
          <div class="caja">
            <p>{nombre}</p>
          </div>
          <div class="caja">
            <img
              class="FotoDeLaBici" src="{imagen}" alt = "Foto de la bici">
          </div>
          <div class="caja">
            <p><b>Localización: </b>{localizacion}</p>
          </div>
          <div class="caja">
            <p><b>Precio: </b>{precio}</p>
          </div>
          <div class="caja">
            <a href="Bici{id}.html">Más detalles</a>
          </div>
        </div>
      </section>""".format(nombre=i["Nombre"], imagen=i["Imagen"], localizacion=i["Localizacion"], precio=i["Precio"], id=i["id"])
    html += """
    </div>
  </body>
</html>"""
    crearHTML("docs/MOMA", html)


def marcaNTT(datos):
    html = """
<!DOCTYPE html>
<html lang="ES" dir="ltr">
  <head>
    <link href="css/OtherPages.css" rel="stylesheet" type="text/css">
    <link rel="icon" href="Img/favicon.png">
    <title>BIBIKES - Marca - NTT</title>
    <meta name="description" content="Pagina del catálogo de marcas disponibles">
    <meta charset="UTF-8">
    <meta name="author" content="Juan Pérez & José Luis De Jesús">
    <meta name="copyright" content="CIFP Francesc de Borja Moll">
    <meta name="generator" content="Visual Studio Code">
    <meta name="keywords" content="Bicis, Carretera, Montaña, Ciudad, Marcas">
    <base target="_blank">
  </head>

  <body class="body">
    <header
      style="
        background: url(Img/banner.jpg);
        background-size: cover;
        background-repeat: no-repeat;
      "
    >
      <!--Esto es el header-->
      <section class="cabecera">
        <br><br>
        <h1>BIBIKES</h1>
        <br><br>
      </section>
      <div class="content">
        <p>Todos los tipos de bicicletas disponibles bajo un mismo techo</p>
        <br><br>
      </div>
    </header>
    <!--Esto es el header-->
    <br>
    <div>
      <h2>Bicicletas disponibles</h2>
    </div>
    <br><br>
     <div id="flex-container">"""
    for i in datos:
        if i["Caracteristicas"]["Marca"] == "NTT":
            html += """
      <section>
        <div class="prueba">
          <div class="caja">
            <p>{nombre}</p>
          </div>
          <div class="caja">
            <img
              class="FotoDeLaBici" src="{imagen}" alt = "Foto de la bici">
          </div>
          <div class="caja">
            <p><b>Localización: </b>{localizacion}</p>
          </div>
          <div class="caja">
            <p><b>Precio: </b>{precio}</p>
          </div>
          <div class="caja">
            <a href="Bici{id}.html">Más detalles</a>
          </div>
        </div>
      </section>""".format(nombre=i["Nombre"], imagen=i["Imagen"], localizacion=i["Localizacion"], precio=i["Precio"], id=i["id"])
    html += """
    </div>
  </body>
</html>"""
    crearHTML("docs/NTT", html)
