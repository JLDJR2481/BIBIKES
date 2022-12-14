import json


def crearHTML(title, content):
    with open(title + ".html", "w+", encoding="UTF-8") as f:
        f.write(content)
        print("Archivo HTML creado")


def paginaIndice():
    html = f"""
<!DOCTYPE html>
<html lang="ES" dir="ltr">
  <head>
    <!--Esto es el head-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link
      href="css/Indice.css"
      rel="stylesheet"
      type="text/css"
      media="screen and (max-width: 800px)">
      <link
      href="css/Indice.css"
      rel="stylesheet"
      type="text/css"
      media="screen and ((min-width: 801px) and (max-width: 1850px))">
    <link
      href="css/Indice.css"
      rel="stylesheet"
      type="text/css"
      media="screen and (min-width: 1851px)">

    <link rel="icon" href="Img/favicon.png">

    <title>BIBIKES - Indice</title>
    <meta name="description" content="Página principal de BIBIKES">
    <meta charset="UTF-8">
    <meta name="author" content="Juan Pérez & José Luis De Jesús">
    <meta name="copyright" content="CIFP Francesc de Borja Moll">
    <meta name="generator" content="Visual Studio Code">
    <meta name="keywords" content="Bicis, Carretera, Montaña, Ciudad, Marcas">
    <base target="_blank">
  </head>
  <!--Esto es el head-->

  <body class="body">
    <!--Esto es el body-->

    <header
      style="
        background: url(Img/banner.jpg);
        background-size: cover;
        background-repeat: no-repeat;
      ">
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
    <div id="Encajar">
      <section class="bicicletas_1">
        <br>

        <!--Section de las bicis de montaña-->
        <div>
          <div id="Montaña">
            <p class="TituloBiciMontaña">
              <span class="TituloBiciMontaña">
                <b>La mejor manera de disfrutar los senderos que ofrece nuestra isla</b>
              </span>
            </p>
            <br>
          </div>

          <div>
            <img
              class="FotoBiciMont"
              src="Img/bici_montaña.jpg"
              height="400"
              width="550"
              alt="Foto bicicleta de montaña">
              <br><br><br>
          </div>

          <div class="TextosMontaña">
            <p class="TextoBiciMontaña">
              En BIBIKES queremos que disfrutes de la naturaleza de Mallorca y
              por ello te ofrecemos las mejores bicis que puedas encontrar en la
              isla
            </p>
            <p class="TextoBiciMontaña">
              Nuestro buscador te ofrece variedad para que escojas la bicicleta
              que más se adapte a tus requisitos personales y te aventures con
              ella a descubrir Mallorca
            </p>
            <br><br>
            <a href="Montaña.html" class="enlaces_catalogo">Ver bicicletas de montaña</a>
          </div>
        </div>
        <br>
      </section>
      <br><br><br><br>

      <!--Section de las bicis de carretera-->
      <section class="bicicletas_1">
        <br>
        <div>
          <div id="Carretera">
            <p class="TituloBiciCarr">
              <b>Siente la brisa de la carretera en las mejores bicicletas</b>
            </p>
            <br>
          </div>
          <div>
            <img
              class="FotoBiciCarr"
              src="Img/bici_carretera.jpg"
              height="400"
              width="550"
              alt="Foto bicicleta de carretera">
           <br><br><br>
          </div>
          <div class="TextosCarretera">
            <p class="TextoBiciCarr">
              Recorre la isla con las mejores bicis que puedas imaginar para
              hacer grandes vueltas por carretera con una gran comodidad con las
              mejores marcas
            </p>
            <p class="TextoBiciCarr">
              Siéntete répido y ágil con unas bicis ligeras preparadas para
              largos recorridos
            </p>
            <br><br>
            <a href="Carretera.html" class="enlaces_catalogo">Ver bicicletas de carretera</a>
          </div>
        </div>
        <br>
      </section>
      <br><br><br><br>
      <section class="bicicletas_1">
        <br>
        <!--Section de las bicis de ciudad-->
        <div class="Montaña">
          <div>
            <p class="TituloBiciCiudad">
              <b>Recorre las calles con calidad y comodidad</b>
            </p>
            <br>
          </div>
          <div>
            <img
              class="FotoBiciCiudad"
              src="Img/bici_ciudad.jpg"
              height="400"
              width="550"
              alt="Foto bicicleta de ciudad">
           <br><br><br>
          </div>
          <div class="TextosCiudad">
            <p class="TextoBiciCiudad">
              Las bicicletas de ciudad ofrecen comodidad y sencillez para
              desenvolverte por las calles de tu ciudad favorita en un abrir y
              cerrar de ojos
            </p>
            <p class="TextoBiciCiudad">
              Con BIBIKES puedes escoger la que más se adapte a ti sin
              complicaciones para poder empezar rápidamente con tu recorrido en
              el sitio que te encuentres
            </p>
            <br><br>
            <a href="Ciudad.html" class="enlaces_catalogo">Ver bicicletas de ciudad</a>
          </div>
          <br>
        </div>
      </section>
    </div>
    <br><br>
    <section id="flex-container2">
      <div>
        <table id="TablaMarcas">
          <tr>
            <th class="Fila2" colspan="9"><b>Marcas disponibles</b></th>
          </tr>
          <tr>
            <td class="Fila2">
              <a href="Riverside.html">Riverside</a>
            </td>
            <td class="Fila2">
              <a href="CERES.html">CERES</a>
            </td>
            <td class="Fila2">
              <a href="BTWIN.html">BTWIN</a>
            </td>
            <td class="Fila2">
              <a href="Rockrider.html">Rockrider</a>
            </td>
            <td class="Fila2">
              <a href="VanRysel.html">Van Rysel</a>
            </td>
            <td class="Fila2">
              <a href="Elops.html">Elops</a>
            </td>
            <td class="Fila2">
              <a href="Triban.html">Triban</a>
            </td>
            <td class="Fila2">
              <a href="MOMA.html">MOMA</a>
            </td>
            <td class="Fila2">
              <a href="NTT.html">NTT</a>
            </td>
          </tr>
        </table>
      </div>
    </section>
    <br>
    <hr>
    <footer>
      <p>Creado por Juan Pérez Moreno y Jose Luis De Jesús</p>
    </footer>
  </body>
  <!--Esto es el body-->
</html>"""
    crearHTML("docs/index", html)
