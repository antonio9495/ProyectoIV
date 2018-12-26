# ProyectoIV

Repositorio para el proyecto a desarrollar para la asignatura de Infraestructuras Virtuales.
[Página de la documentación](https://antonioj95.github.io/ProyectoIV/)

## Descripción
Creación de microservicios que permita gestionar una relación de una serie de actividades y eventos a unas coordenadas específicas.
El microservicio principal consistirá en añadir una tarea a una localización.

El proyecto completo sobre el que podría ir sería una aplicación de agenda diaria sobre la cual los eventos se unirían a ciertas localizaciones permitiendo que estos se activarán según lleguen a una localización o para ver los eventos que se tienen que realizar en una localización específica.

## Herramientas
- Lenguaje de programación: [Python](https://www.python.org/).

- Framework: [Flask](http://flask.pocoo.org/).

- Base de datos: [MongoDB](https://www.mongodb.com/).

- Automatización: [Heroku](https://www.heroku.com/), [Docker](https://www.docker.com/) y [Travis](https://travis-ci.org/).

- Creación de test: [Pytest](https://docs.pytest.org/en/latest/).

## Descripción de la clase
La clase contiene un diccionario el cual almacena objetos con actividades y localizaciones relacionadas.
Las actividades constan de un identificador, un titulo y un tipo.
Las localizaciones constan de un identificador, latitud y longitud.
Con la clase podremos buscar localización y actividades según su identificador, ver las localización con las que se relaciona una actividad y viceversa y añadir un objeto nuevo que relacione una localización con una actividad .

## Integración continua
Utilizamos Travis como sistema de integración contínua encargado de lanzar los tests. Tenemos ya Travis enlazado con la cuenta de github.

### Instalación
`pip3 install -r requirements.txt`

### Ejecutar tests
`pytest`

### Ejecutar programa
`phyton3 src/Prueba.py`

### Despliegue [![](https://www.herokucdn.com/deploy/button.svg)](https://mysterious-bastion-92654.herokuapp.com/)

*  Enlace al despliegue provisional:[Despliegue](https://mysterious-bastion-92654.herokuapp.com/)

El despligue lo hemos realizado usando Heroku ya que nos aporta integración con GitHub y Travis facilitandonos así la integración continua.

Para ello hemos tenido que registrarnos en la web de Heroku, una vez registrados con la cuenta de correo de GitHub nos permite buscar nuestro repositorio de GitHub para así vincularlo.

En el apartado de Deploy podemos seleccionar la opción de desplegar automáticamente para poder permitir que cada push al proyecto en la rama elegida, en mi caso la master, haga que se implemente una nueva versión.

Importante seleccionar la casilla para que espere a los test de travis antes de realizar esto.

Aparte de añadir un **archivo Procfile** con el que especificaremos los comandos que serán ejecutados por los dynos de Heroku.
En el añadiremos una linea indicando que para el proceso web se aplique el comando gunicorn application:app

Para comprobar el funcionamiento podemos realizar diversas operaciones como:
- Obtener el valor de un dato: [/getInfoDato/idobjeto1](https://mysterious-bastion-92654.herokuapp.com/getInfoDato/idobjeto1).
> Añadiendo en la url /getInfoDato/el_id_objeto_dato nos muestra todos los elementos que componen ese dato junto a su información

- Obtener una posición específica y sus actividades relacionadas: [/searchP/Pos1](https://mysterious-bastion-92654.herokuapp.com/searchP/Pos1).
> Añadiendo en la url /searchP/el_id_de_la_posición nos muestra los datos que componen esa posición junto a los ids de las actividades que se relacionan con esta posición

- Obtener una actividad específica y sus posiciones relacionadas: [/searchA/Act1](https://mysterious-bastion-92654.herokuapp.com/searchA/Act1).
> Añadiendo en la url /searchA/actividad nos muestra los datos que componen esa actividad junto a los ids de las posiciones que se relacionan con esta actividad

### Despliegue en contenedor [![](https://www.herokucdn.com/deploy/button.svg)](https://docker-iv-project.herokuapp.com)

Enlace a [DockerHub](https://hub.docker.com/r/ajimenez95/projectiv)

Este repositorio está creado usando la opción de Create Automated Build, linkando nuestra cuenta de github y seleccionando nuestro repositorio del proyecto.
Con esto conseguimos que se construya una imagen de docker cada vez que se hace un push al repositorio usando el Dockerfile que se encuentra en github.

En el Dockerfile indicamos los archivos que necesitamos copiar, que instale las dependencias que tenemos en requirements.txt y la orden a ejecutar.

Para que nuestra nueva app de heroku construya la imagen de docker añadimos el heroku.yml y le indicamos con heroku stack:set container que utilizaremoss docker.


## Licencia
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/antonioJ95/ProyectoIV/blob/master/LICENSE)
## Tests
[![Build Status](https://travis-ci.org/antonioJ95/ProyectoIV.svg?branch=master)](https://travis-ci.org/antonioJ95/ProyectoIV)