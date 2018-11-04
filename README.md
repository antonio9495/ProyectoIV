# ProyectoIV

Repositorio para el proyecto a desarrollar para la asignatura de Infraestructuras Virtuales.
[Página de la documentación](https://antonioj95.github.io/ProyectoIV/)

## Descripción
Creación de microservicios que permita gestionar una relación de una serie de actividades y eventos a unas coordenadas específicas.
El microservicio principal consistirá en añadir una tarea a una localización.

El proyecto completo sobre el que podría ir sería una aplicación de agenda diaria sobre la cual los eventos se unirían a ciertas localizaciones permitiendo que estos se activarán según lleguen a una localización o para ver los eventos que se tienen que realizar en una localización específica.

## Herramientas
- Lenguaje de programación: [Python](https://www.python.org/).
> Esta elección se basa en la gran demanda que tiene Python hoy en día, junto a la gran potencia y cantidad de librerías de las que dispone para facilitar el trabajo con el.

- Framework: [Flask](http://flask.pocoo.org/).
> La elección de este framework va de la mano con la elección del lenguaje ya que se trata de un microframework perfecto para realizar pequeños proyectos que se encuentra muy bien integrado con Python.

- Base de datos: [MongoDB](https://www.mongodb.com/).
> Es una base de datos no relacional de las más conocidas y que trabaja con los datos como si fueran JSONs. Algo que he visto muy interesante de cara a la asignatura y de provecho para entender el trabajo con este tipo de datos.

- Automatización del despliegue: [Heroku](https://www.heroku.com/), [Docker](https://www.docker.com/) y [Travis](https://travis-ci.org/).
> Docker será usado para la contenerización del microservicio obteniendo así un contenedor virtual que podremos ejecutar directamente en la Infraestructura que nos proporcione Heroku y utilizando Travis para la integración continua.

- Creación de test: [Pytest](https://docs.pytest.org/en/latest/).
> Es un framework sencillo para Python que permite de una forma sencilla la creación de pequeños tests.

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

### Despligue  [![](https://www.herokucdn.com/deploy/button.svg)](https://mysterious-bastion-92654.herokuapp.com/)

Para comprobar el funcionamiento podemos realizar diversas operaciones como:
- Obtener el valor de un dato: [/getInfoDato/idobjeto1](https://mysterious-bastion-92654.herokuapp.com/getInfoDato/idobjeto1).
> Añadiendo en la url /getInfoDato/el_id_objeto_dato nos muestra todos los elementos que componen ese dato junto a su información

- Obtener una posición específica y sus actividades relacionadas: [/searchP/idPos](https://mysterious-bastion-92654.herokuapp.com/searchP/Pos1).
> Añadiendo en la url /searchP/el_id_de_la_posición nos muestra los datos que componen esa posición junto a los ids de las actividades que se relacionan con esta posición

- Obtener una actividad específica y sus posiciones relacionadas: [/searchA/idAct](https://mysterious-bastion-92654.herokuapp.com/searchA/Act1).
> Añadiendo en la url /searchA/actividad nos muestra los datos que componen esa actividad junto a los ids de las posiciones que se relacionan con esta actividad

## Licencia
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/antonioJ95/ProyectoIV/blob/master/LICENSE)
## Tests
[![Build Status](https://travis-ci.org/antonioJ95/ProyectoIV.svg?branch=master)](https://travis-ci.org/antonioJ95/ProyectoIV)
