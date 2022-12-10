import json


def crearHTML(title, content):
    with open(title + ".html", "w+", encoding="UTF-8") as f:
        f.write(content)
        print("Archivo HTML creado")


def PaginaCarretera(datos):
    html = f"""
<!DOCTYPE html>
<html lang="ES" dir="ltr">
  <head>
    <link href="css/OtherPages.css" rel="stylesheet" type="text/css">
    <link rel="icon" href="img/favicon.png">
    <title>BIBIKES - Bicicletas de carretera</title>
    <meta name="description" content="Pagina del catálogo de bicicletas de carretera">
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
        background: url(img/banner.jpg);
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
    <div id="flex-container">
    """
    for i in datos:
        if i.get("Tipo") == "Bicicleta de Carretera":
            html += """
      <section>
        <div class="prueba">
          <div class="caja">
            <p>{Nombre}</p>
          </div>
          <div class="caja">
            <img
              class="FotoDeLaBici" src="{Imagen}" alt = "Foto de la bici">
          </div>
          <div class="caja">
            <p><b>Localización: </b>{Localizacion}</p>
          </div>
          <div class="caja">
            <p><b>Precio: </b>{Precio}</p>
          </div>
          <div class="caja">
            <a href="Bici{id}.html">Más detalles</a>
          </div>
        </div>
      </section>""".format(Nombre=i.get("Nombre"), Imagen=i.get("Imagen"), Localizacion=i.get("Localizacion"), Precio=i.get("Precio"), id=i.get("id"))
    html += """
    </div>
  </body>
</html>"""

    crearHTML("docs/Carretera", html)
