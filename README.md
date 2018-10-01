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

- Framework: [Django](https://www.djangoproject.com/).
> La elección de este framework va de la mano con la elección del lenguaje ya que es uno de los más utilizados y demandados para Python y facilita bastante la creación de una interfaz de forma simple.

- Base de datos: [MongoDB](https://www.mongodb.com/).
> Es una base de datos no relacional de las más conocidas y que trabaja con los datos como si fueran JSONs. Algo que he visto muy interesante de cara a la asignatura y de provecho para entender el trabajo con este tipo de datos.

- Automatización del despliegue: [Azure](https://azure.microsoft.com/en-us/), [Docker](https://www.docker.com/) y [Travis](https://travis-ci.org/).
> Docker será usado para la contenerización del microservicio obteniendo así un contenedor virtual que podremos ejecutar directamente en la Infraestructura que nos proporcione Azure y utilizando Travis para la integración continua.

- Creación de test: [Pytest](https://docs.pytest.org/en/latest/).
> Es un framework sencillo para Python que permite de una forma sencilla la creación de pequeños tests.

## Licencia
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/antonioJ95/ProyectoIV/blob/master/LICENSE)
