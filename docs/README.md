# ProyectoIV

### Despliegue [![](https://www.herokucdn.com/deploy/button.svg)](https://mysterious-bastion-92654.herokuapp.com/)

*  Enlace al despliegue provisional:[Despliegue](https://mysterious-bastion-92654.herokuapp.com/)

El despliegue lo hemos realizado usando Heroku ya que nos aporta integración con GitHub y Travis facilitandonos así la integración continua.

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

#### Dockerfile:
Con el Dockerfile estamos indicando tanto la imagen base que utilizaremos para nuestro contenedor como las instrucciones necesarias para cubrir las necesidades de nuestra app.

En nuestro Dockerfile indicamos la imagen que usamos como base (python:3.6), indicamos los archivos que necesitamos copiar, que instale las dependencias que tenemos en requirements.txt y el comando de inicio a usar cuando inicie el contenedor.

La imagen base utilizada es la versión de python que tengo en mi ordenador, la cual incluye los paquetes necesarios para el funcionamiento de mi app y con la que tengo comprobado que funciona.


#### DockerHub
El repositorio de DockerHub está creado una vez nos hemos registrados en DockerHub y usando la opción de Create Automated Build.
Esta opción nos permite enlazar nuestra cuenta de Github y seleccionar nuestro repositorio del proyecto, para poder acceder al Dockerfile contenido en el, y crear así una imagen con cada push que realicemos a nuestro repositorio de Github.
Esta imagen se almacenará en este repositorio de DockerHub.


La configuración en el apartado builds de nuestro repositorio de DockerHub debe ser la siguiente:
![img](https://github.com/antonioJ95/ProyectoIV/tree/master/docs/configuracionDockerHub.png)

Con esta cofiguración ya tendríamos asegurado que este repositorio de DockerHub esta enlazado con el nuestro de GitHub en el cual se encuentra nuestro proyecto y le tenemos indicada también donde está el dockerfile que debe de utilizar.


#### Heroku.yml y despliegue con contenedor:
[Documentación seguida](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)

Hemos creado otra app en heroku para desplegar la usando contenedores.
![img](https://github.com/antonioJ95/ProyectoIV/tree/master/docs/aps.png)

Para que nuestra nueva app de heroku construya una imagen docker añadimos el heroku.yml, donde le indicamos en la parte de build que usaremos el Dockerfile que se encuentra en este directorio y en la parte de run la orden que debe de ejecutar para lanzar la app.
En el heroku.yml en caso de no indicar ninguna orden para la ejecución en la sección run se utiliza la especificada en la parte de CMD del Dockerfile.

Nuestra nueva app esta conectada también con nuestro repositorio de GitHub de la siguiente forma:
![img](https://github.com/antonioJ95/ProyectoIV/tree/master/docs/appsconf.png)

Pero para que heroku utilice el heoroku.yml en lugar del procfile, debemos de indicárselo desde terminal usando el heroku cli.

Esto se realiza usando el siguiente comando:
~~~
heroku stack:set container
~~~
Con esto le indicamos a Heroku que el desliegue de la app  se realizará usando contenedores y pillando así el heroku.yml.

Podemos ver que esto se ha realizado correctamente en la información de nuestra nueva app desde el dashboard de Heroku:
![img](https://github.com/antonioJ95/ProyectoIV/tree/master/docs/herokuStack.png)

O desde nuestro ordenador usando el comando:
~~~
heroku apps:info docker-iv-project
~~~
![img](https://github.com/antonioJ95/ProyectoIV/tree/master/docs/apsterminal.png)

Donde en ambas partes vemos que en Stack pone container.


## Licencia
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/antonioJ95/ProyectoIV/blob/master/LICENSE)
## Tests
[![Build Status](https://travis-ci.org/antonioJ95/ProyectoIV.svg?branch=master)](https://travis-ci.org/antonioJ95/ProyectoIV)