# ProyectoIV

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

#### DockerHub y Dockerfile:
El repositorio enlazado arriba está creado una vez nos hemos registrados en DockerHub y usando la opción de Create Automated Build.
Esta opción nos permite enlazar nuestra cuenta de Github, seleccionar nuestro repositorio del proyecto, para poder acceder al Dockerfile contenido en el, y crear así una imagen con cada push que realicemos a nuestro repositorio de Github.

Con el Dockerfile estamos indicando tanto la imagen base que utilizaremos como las instrucciones para construir el contenedor.
En nuestro Dockerfile indicamos la imagen que usamos como base (python:3.6), indicamos los archivos que necesitamos copiar, que instale las dependencias que tenemos en requirements.txt y el comando de inicio a usar cuando inicie el contenedor.
La imagen base utilizada es la versión de python que tengo en mi ordenador, la cual incluye los paquetes necesarios para el funcionamiento de mi app y con la que tengo comprobado que funciona.


#### Heroku.yml:
[Documentación seguida](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)

Hemos creado otra app en heroku para desplegar la usando contenedores.
Para que nuestra nueva app de heroku construya la imagen de docker añadimos el heroku.yml donde le indicamos en la parte de build que usaremos el Dockerfile que se encuentra en este directorio.
Y le indicamos con heroku stack:set container que utilizaremos contenedores para esta app.

En el heroku.yml no hemos indicado ninguna orden para la ejecución ya que como indica la documentación se puede utilizar la que ya se encuentra en el Dockerfile.


## Licencia
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/antonioJ95/ProyectoIV/blob/master/LICENSE)
## Tests
[![Build Status](https://travis-ci.org/antonioJ95/ProyectoIV.svg?branch=master)](https://travis-ci.org/antonioJ95/ProyectoIV)