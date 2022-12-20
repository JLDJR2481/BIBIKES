import json


def crearHTML(title, content):
    with open(title + ".html", "w", encoding="UTF-8") as f:
        f.write(content)
        print("Archivo HTML creado")


def bicisIndividuales(datos):
    appeared = []
    for i in datos:
        if i["id"] not in appeared:
            html = """
<!DOCTYPE html>
<html lang="ES" dir="ltr">
  <head>
    <link href="css/OtherPages.css" rel="stylesheet" type="text/css">
    <link rel="icon" href="Img/favicon.png">
    <title>BIBIKES - Información</title>
    <meta name="description" content="Pagina de información de cada bicicleta">
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
        <h1>BI-BIKES</h1>
        <br><br>
      </section>
      <div class="content">
        <p>Todos los tipos de bicicletas disponibles bajo un mismo techo</p>
        <br><br>
      </div>
    </header>
    <!--Esto es el header-->
    <br>
    <section id="flex-container">
      <div class="prueba">
        <div class="caja">
          <p><b> {Nombre} </b> </p>
        </div >
        <div class = "caja" >
          <img
            class = "FotoDeLaBici"
            src ="{Imagen}"
            alt = "Foto de la bici">
        </div>
        <div class = "caja">
          <p> <b> Marca: </b> {Marca} </p>
        </div>
        <div class= "caja">
          <p> <b> Talla: </b> {Talla} </p>
        </div >
        <div class= "caja" >
          <p > <b > Cuadro: </b> {Cuadro} </p>
        </div >
        <div class= "caja" >
          <p > <b > Suspension:</b> {Suspension} </p>
        </div >
        <div class= "caja" >
          <p > <b > Tamaño de rueda:</b> {Tamaño_de_ruedas} </p>
        </div >
        <div class= "caja" >
          <p > <b > Velocidades:</b> {Velocidades} </p>
        </div >
        <div class= "caja" >
          <p > <b > Material:</b> {Material} </p>
        </div >
        <div class= "caja" >
          <a href="formulario.html"> Alquilar </a >
        </div >
      </div>
    </section>
    <br>
  </body >
</html>""".format(Nombre=i.get("Nombre"), Imagen=i.get("Imagen"), Marca=i["Caracteristicas"]["Marca"], Talla=i["Caracteristicas"]["Talla"], Cuadro=i["Caracteristicas"]["Cuadro"], Suspension=i["Caracteristicas"]["Suspension"], Tamaño_de_ruedas=i["Caracteristicas"]["Tamaño ruedas"], Velocidades=i["Caracteristicas"]["Velocidades"], Material=i["Caracteristicas"]["Material"])

            appeared.append(i["id"])
            crearHTML("docs/Bici" + str(i["id"]), html)
