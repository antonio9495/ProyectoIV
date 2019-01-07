# ProyectoIV

Repositorio para el proyecto a desarrollar para la asignatura de Infraestructuras Virtuales.

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

### Despliegue [![](https://www.herokucdn.com/deploy/button.svg)](https://mysterious-bastion-92654.herokuapp.com/)

*  Enlace al despliegue provisional:[Despliegue](https://mysterious-bastion-92654.herokuapp.com/)


### Despliegue en contenedor [![](https://www.herokucdn.com/deploy/button.svg)](https://docker-iv-project.herokuapp.com)

Enlace a [DockerHub](https://hub.docker.com/r/ajimenez95/projectiv)

[Página de la documentación](https://antonioj95.github.io/ProyectoIV/)
## Licencia
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/antonioJ95/ProyectoIV/blob/master/LICENSE)
## Tests
[![Build Status](https://travis-ci.org/antonioJ95/ProyectoIV.svg?branch=master)](https://travis-ci.org/antonioJ95/ProyectoIV)