# BIBIKES

## **Indice**
- [**BIBIKES**](#bibikes)
- [**Introducción**](#introducción)
- [**Pre-requisitos**](#pre-requisitos)
    - [**Instalación**](#instalación)
    - [**Uso**](#uso)
- [**Descripción Técnica**](#descripción-técnica)
    - [**Arquitectura de la aplicación**](#arquitectura-de-la-aplicación)
    - [**Tecnologías y herramientas utilizadas**](#tecnologías-y-herramientas-utilizadas)
    - [**Diagrama de componentes**](#diagrama-de-componentes)
    - [**Diagrama base de datos**](#diagrama-base-de-datos)
- [**Metodología**](#metodología)
- [**Pruebas**](#pruebas)
- [**Clockify**](#clockify)
    - [**Diagrama Barras**](#diagrama-barras)
    - [**Diagrama Circular**](#diagrama-circular)
- [**Mejoras**](#mejoras)
- [**Dificultades**](#dificultades)
- [**Información extra**](#información-extra)
    - [**Gráfico de Ramas**](#gráfico-de-ramas)
    - [**Contribuidores**](#contribuidores)

## BIBIKES
**BIBIKES** nace de un problema grave ubicado en las Islas Baleares: hay demasiada contaminación por exceso de vehículos. Para ello, se ha desarrollado una plataforma de alquiler de bicis la cual permite alquilar de una forma sencilla y con un diseño simple pero llamativo.

Para poder crear esta plataforma, hemos utilizado un servicio de MongoDB llamado [**MongoAtlas**](https://www.mongodb.com/es/cloud/atlas/efficiency)
Además, hemos utilizado un lenguaje de programación que la gran mayoría conocemos, [**PYTHON**](https://www.python.org/) con la version 3.10.7.
Por ultimo, hemos usado el servicio ofrecido por GitHub conocido como GitHub Pages, que nos permite poder visualizar nuestro sitio web


## Introducción
Es el mes de abril y acabas de aterrizar en el departamento de desarrollo de tu flamante nueva empresa de Dual.
Ahora toca trabajar y en tu empresa han decidido que bas a **desarrollar un mínimo producto viable**, una idea de negocio a la que llevan dando vueltas tiempo y procrastinando, aplicando estos conocimientos, y así que les enseñes lo que tienes sin romper nada (además de ganarte tu primer salario). 

El excesivo número de coches en las carreteras de Baleares se ha convertido en un problema, el Gobierno de las Islas Baleares está barajando diversas medidas.
La idea es crear una plataforma donde la gente local y los/as turistas puedan chequear la disponibilidad de bicicletas de alquiler en un área. Se trata de construir un agregador donde las compañías volcasen su flota de bicicletas. 

Tu empresa quiere poner en marcha un site que muestre información sobre un modelo concreto de bicicleta, dónde se encuentra disponible en alquiler y realizar comparativas entre las características de diferentes modelos. Cada bicicleta se encuentra en stock en una empresa de alquiler distinta. La idea es vender este producto como un agregador de las bicicletas disponibles en los negocios de alquiler de les Illes Balears.

**REQUISITOS**
Tu tutor/a de empresa quiere:
- Desarrolla una aplicación **Python** para extraer los datos de **MongoAtlas**. Se hace necesario diseñar una especificación del esquema de los documentos **JSON**.
- Esos documentos **JSON** tendrás que transformarlos, también con una aplicación **Python**, en ficheros **HTML** (los estilos **CSS** corren también por tu cuenta). 
- Luego, has de situar estos ficheros en una estructura de directorios que establece el generador de sitios estáticos de **GitHub Pages**, también mediante una aplicación **Python** que construyas.
- Cuando subas este código a tu repo en github, **GitHub Pages** servirá las páginas **HTML** a modo de sitio web estático.
- Tendrás que customizar los estilos **CSS** para dar la presentación adecuada a los datos.
- Desarrolla una **API** de **MongoAtlas** que permita hacer un **CRUD**.

## Pre-requisitos
```
- Python3
- pip3
- Git
- Requests
- pytest
```

### Instalación
Se recomienda el uso de un entorno virtual (venv) que permita tener instaladas las dependencias utilizadas en el proyecto.

### Uso
Para BIBIKES, hemos decidido tener una gran funcion main.py el cual permita generar lo necesario para la creación de BIBIKES.

[MAS INFORMACIÓN](https://github.com/JLDJR2481/BIBIKES/tree/main/src)

## Descripción técnica
### Arquitectura de la aplicación
![Arquitectura de la aplicacion](https://user-images.githubusercontent.com/115024410/207160589-3f34071a-0ac8-4079-a166-16d9aee83ee1.jpg)

### Tecnologías y herramientas utilizadas
- **[Python](https://www.python.org/)**
  - **[OS](https://docs.python.org/3/library/os.html)** Se trata de una libreria incorporada de Python que nos permite acceder a funciones dependientes del Sistema Operativo
  - **[REQUEST](https://requests.readthedocs.io/en/latest/)** Nos ayuda a trabajar con peticiones HTTP
  - **[PYTEST](https://docs.pytest.org/en/7.2.x/)** Para realizar pruebas unitarias en un software con Python
  - **[JSON](https://docs.python.org/3/library/json.html)** Libreria para poder trabajar con documentos en formato JSON transformandolo en diccionario o lista de Python
- **[MONGODB](https://www.mongodb.com/docs/)**
  - **[MongoAtlas](https://www.mongodb.com/es/cloud/atlas/efficiency)** Se trata del servicio de Base de Datos en la Nube que nos permite crear y administrar una base de datos Mongo
  - **[MongoDB API](https://www.mongodb.com/docs/atlas/api/)** Herramienta que nos permite usar APIS para interactuar con MongoAtlas
- **[HTML5](https://www.w3schools.com/html/html_intro.asp)** y **[CSS3](https://www.w3schools.com/css/css_intro.asp)** Lenguajes que dan formato a las paginas webs
- [Git](https://git-scm.com/docs) Sistema para el control de versiones
- [MarkDown](https://markdown.es/) Lenguaje de marcas ligero
- [GitHub Pages](https://pages.github.com/) Servicio que ofrece GitHub para alojar nuestros sitios estaticos desde un repositorio en GitHub


### Diagrama de componentes
![Diagrama de componentes](https://user-images.githubusercontent.com/115024410/207161158-439e66e7-bdfc-4f3c-a53b-7861a67d3288.jpg)
Nuestro diagrama de componentes se divide en:
- **Base de datos**
  - Create: Permite crear una nueva bici desde 0
  - Read: Permite buscar alguna bici por su id
  - Update: Nos permite modificar ciertos datos de una bici en concreto
  - Delete: Nos permite borrar las bicis que queramos
  - Conexion: Nos permite conectarnos a la Base de Datos y actualizarla
  - Importar datos: Nos permite importar los datos

- **JSON** (Ubicado en el main)
  - Archivo JSON: Nos permite crear un archivo
  - Transformar JSON: Nos permite transformarlo para trabajar en 
  
- **HTML & CSS**
  - Index: Crea un indice
  - Tipos: Crea varios archivos filtrando por tipos
  - Marcas: Crea varios archivos filtrando por marcas
  - Bici: Crea un archivo por cada bici que exista en la base de datos
  
- **Ver páginas**: Nos permite cargar y visualizar las páginas creadas con HTML y CSS

### Diagrama base de datos
La base de datos vinculada a BIBIKES recoge la siguiente información:
![Diagrama de Base de Datos](https://user-images.githubusercontent.com/115024410/207161731-7f0c112b-716f-40ae-8490-eeb743ec7507.jpg)

## Metodología
Para este proyecto, hemos optado por una metodología Ágil. Es decir:
  1. Hemos discutido y planificado nuestros objetivos
  2. Hemos empezado haciendo el diseño
  3. Hemos empezado a codificar y realizar pruebas
  4. Hemos implementado nuestro codigo para que empiece a iterar
  5. Tras ello, hemos comentado que podríamos mejorar y que errores podrían salir
  
Aunque sea una metodología que permite realizar los desarrollos en el menor de los tiempos, nos hemos encontrado con varios problemas tanto en el codigo como en el diseño de nuestras paginas webs.

## Pruebas
Nuestras pruebas, que sobretodo estan ubicados en la carpeta test, se basan en confirmaciones tanto de rutas como de archivos. Nos hemos asegurado que cada archivo que se haya creado con Python. Aquí os mostramos un ejemplo
```
def test_comprobarRutaArchivoJSON():
    assert os.path.exists(rutaJSON) != False
```
Además, estan configurados de tal forma que usando pytest recoge todos los casos test que se encuentran en el codigo, y detecta si algun archivo importante, como index.html o Bicis.json tiene su ruta correspondiente y, además, confirmar que es un archivo con contenido

## Clockify
Para computar el tiempo dedicado, hemos dividido el tiempo dedicado a las distintas asignaturas con las que hemos trabajado con sus colores en concretos. El tiempo utilizado al aprendizaje de nuevas posibilidades para implementar a nuestro codigo y de entendimiento sobre, por ejemplo, el uso de GitHub Pages no han sido computados.
Además, las asignaturas han sido divididas en proyectos, para más facilitación de entendimiento y uso de la aplicación

### Diagrama barras
![Diagrama de Barras](https://user-images.githubusercontent.com/115024410/207167287-ab56b901-9d85-4184-9c3b-3dd11f5f6c89.png)

### Diagrama Circular
![Diagrama Circular](https://user-images.githubusercontent.com/115024410/207167866-c53d981f-f2d8-40b8-b297-ef9e55fb7adc.png)

## Mejoras
Actualmente, tenemos bastantes mejoras en mente que implementar, como por ejemplo:
- Un mejor sistema de navegación entre páginas, ya que se puede hacer tedioso la navegación de la misma
- Una mejor recogida de datos, ya sea con librerias externas como puede ser Pymongo u otros

## Dificultades
Una de las mayores dificultades que hemos tenido a la hora de trabajar es el poco conocimiento que teniamos sobre el uso de GitHub Page, sobre las ramas, sobre los comandos... Eso nos hizo perder mucho más tiempo, ya que debíamos aprender sin computar, ya que, a vistas de la empresa, no es facturable.

## Información Extra
### Gráfico de Ramas
![Ramas](https://user-images.githubusercontent.com/115024410/207169369-5bd7403f-21fe-4990-91c3-41d1857eb205.PNG)

### Contribuidores
![Contribuidores](https://contrib.rocks/image?repo=JLDJR2481/BIBIKES)








