# CRUD Con DRF y PostGreSQL

## Introducción :rocket:
Este es un aplicativo web tipo REST, que sirve para realizar las operaciones CRUD, sobre información relacionada con películas.

Puertos por defecto.

Cliente: 8000

Servidor: 5432

URL, servicio Web: https://despliegue-crud-drf-postgresql.onrender.com/api/movies/

## Tecnologías utilizadas :heavy_check_mark:
Las principales tecnologías que fueron utilizadas en este proyecto son:

asgiref v 3.7.2
Brotli v 1.1.0
dj-database-url v 2.1.0
Django v 5.0.2
djangorestframework v 3.14.0
djangorestframework-gis v 1.0
gunicorn v 21.2.0
packaging v 23.2
psycopg2-binary v 2.9.9
pytz v 2024.1
sqlparse v 0.4.4
typing_extensions v 4.10.0
tzdata v 2024.1
whitenoise v 6.6.0

## Instalación :heavy_check_mark:
Primero clona el contenido de este repositorio, en una carpeta que tengas destinada para tal fin, después dentro de la carpeta dale click derecho y en Git Bash here o similares. Asegurate que la dirección de la carpeta coincida con dónde quieres que se clone el  repositorio y ejecuta la siguiente instrucción.

'git clone https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql.git'

cuando este sobre la carpeta del proyecto asegurate de ejectutar los siguientes comandos:

1) pip install virtualenv

2) /python -m virtualenv espv

3) .\espv\Scripts\activate

4) django-admin startproject crudrf
El paso 5, es por si vas a desplegar el servidor de prueba de forma local.
5) python manage.py runserver

Listo con estos pasos habrás hecho lo necesario para que la aplicación funcione correctamente. Se te debería abrir una pestaña en tu navegador con la aplicación. En caso de que no se abra automáticamente puedes acceder a ella de forma manual colocando la siguiente dirección en tu navegador.
'http://127.0.0.1:8000/api/movies/'

O UTILIZAR EL SERVICIO WEB DESPLEGADO EN RENDER, ACCEDIENDO MEDIANTE EL LINK
https://despliegue-crud-drf-postgresql.onrender.com/api/movies/


   
