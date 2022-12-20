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
          <p><b> {nombre} </b> </p>
        </div >
        <div class = "caja" >
          <img
            class = "FotoDeLaBici"
            src ="{imagen}"
            alt = "Foto de la bici">
        </div>
        <div class = "caja">
          <p> <b> Marca: </b> {marca} </p>
        </div>
        <div class= "caja">
          <p> <b> Talla: </b> {talla} </p>
        </div >
        <div class= "caja" >
          <p > <b > Cuadro: </b> {cuadro} </p>
        </div >
        <div class= "caja" >
          <p > <b > Suspension:</b> {suspension} </p>
        </div >
        <div class= "caja" >
          <p > <b > Tamaño de rueda:</b> {tamaño_de_ruedas} </p>
        </div >
        <div class= "caja" >
          <p > <b > Velocidades:</b> {velocidades} </p>
        </div >
        <div class= "caja" >
          <p > <b > Material:</b> {material} </p>
        </div >
        <div class= "caja" >
          <a href="formulario.html"> Alquilar </a >
        </div >
      </div>
    </section>
    <br>
  </body >
</html>""".format(nombre=i.get("Nombre"), imagen=i.get("Imagen"), marca=i["Caracteristicas"]["Marca"], talla=i["Caracteristicas"]["Talla"], cuadro=i["Caracteristicas"]["Cuadro"], suspension=i["Caracteristicas"]["Suspension"], tamaño_de_ruedas=i["Caracteristicas"]["Tamaño ruedas"], velocidades=i["Caracteristicas"]["Velocidades"], material=i["Caracteristicas"]["Material"])

            appeared.append(i["id"])
            crearHTML("docs/Bici" + str(i["id"]), html)
