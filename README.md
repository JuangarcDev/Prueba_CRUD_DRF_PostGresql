# CRUD Con DRF y PostGreSQL

## Introducción :rocket:
Este es un aplicativo web tipo REST, que sirve para realizar las operaciones CRUD, sobre información relacionada con películas.

Puertos por defecto.

Cliente: 8000

Servidor: 5432

URL, servicio Web: https://despliegue-crud-drf-postgresql.onrender.com/api/movies/

## Tecnologías utilizadas :heavy_check_mark:
Las principales tecnologías que fueron utilizadas en este proyecto son:

-asgiref v 3.7.2

-Brotli v 1.1.0

-dj-database-url v 2.1.0

-Django v 5.0.2

-djangorestframework v 3.14.0

-djangorestframework-gis v 1.0

-gunicorn v 21.2.0

-packaging v 23.2

-psycopg2-binary v 2.9.9

-pytz v 2024.1

-sqlparse v 0.4.4

-typing_extensions v 4.10.0

-tzdata v 2024.1

-whitenoise v 6.6.0

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

## Endpoints y pruebas Locales Métodos :heavy_check_mark:

Se iba a dividir el modelo de datos en películas y pais. Pero por problemas con el GDAL resulto conveniente dejar el nombre del pais, dentro de película. 

MÉTODO GET LOCAL (ALL)

![1_GET_ALL](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/7f167c0d-e07f-4e52-9235-ec22f4a3c2fe)

/api/movies/
Me lista todas las películas persistidas hasta ese momento. Como se puede apreciar se tenían 5 peliculas persistidas en la BD.

MÉTODO GET LOCAL (UNID)

![2_GET_ONE](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/ce1b5fec-b4bb-4834-8645-68e48d8e47b1)

/api/movies/id
Me lista los valores de la película con el id = 4. Como podemos apreciar se trata de la película Siempreviva.

MÉTODO POST LOCAL

![3_POST_ONE](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/7199f3f3-99ab-40b2-982d-6a01ec61e694)

Se persisten los datos para una nueva película, en este caso la película Porco Rosso, con 4.67 de calificación.

MÉTODO PUT LOCAL

![4_PUT1](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/56324ea9-9c78-40fd-9683-637b5faade3b)

Se modifican los datos de la película identificada con id = 6, se cambia la valoración a 4.77

MÉTODO DELETE LOCAL

![5_DELETE1](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/cfdf4e45-6f7b-47b8-b44b-805e0265c467)

Se elimina el registro de película identificado con el id = 5

## Despliegue RENDER:

Para desplegar el aplicativo en un recurso web se acude a RENDER y se configura con todo lo necesario para ejecutarse, incluyendo la creación de PostGresql desde RENDER y se crean de forma automática mediante el código y la migración que crea las tablas de la BD.

![6_DESPLIEGUE_RENDER](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/7cfa251b-010e-47f2-97c1-54dc1bdc8666)

Como podemos apreciar se aprecia el correcto despliegue del servicio web en RENDER.  Correctamente conectado al presente repositorio y generando el url de acceso.
https://despliegue-crud-drf-postgresql.onrender.com/api/movies/

También podemos apreciar la creación de DB de PostGreSQL 14

![13_CONEXIONES_BD_RENDER](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/163c4f38-87f2-4bb8-8b1e-7801042b3ef9)

## Endpoints y pruebas WEB Métodos :heavy_check_mark:

MÉTODO POST WEB

![7_POST_ONE_WEB](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/70e2c992-8743-46c0-bd8d-cd4b7f351fab)

Como apreciamos, persistimos la película El precio del mañana.  Desde la interfaz propia del DRF.

AHORA DESDE UN AYUDANTE DE SOLICITUDES, TIPO POSTMAN

![8_POST_ONE_WEB](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/a6166956-a146-4fc0-a845-0dc5ad7c7047)


MÉTODO GET WEB (ALL)

![9_GET_ALL_WEB](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/8eb2f726-d942-455a-bb41-335c0767423a)

Vemos que al momento de la consulta solo se contaba con 2 registros de películas dentro de la DB, El precio del mañana y jurassic park.

MÉTODO GET WEB (IND)

![10_GET_ALL_ONE](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/ad993d1a-bc9b-4d0b-b75e-550a9fccb59c)

Vemos que se consulta la película con id=2, la cual corresponde a jurassic park.

MÉTODO PUT WEB

![11_PUT1](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/15a96d58-da87-4033-82da-c9adc9b590d2)

Como podemos ver modificamos la película que tiene el id =2, se le cambia su calificacion a 4.60

MÉTODO DELETE WEB

![12_DELETE1](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/d3f744f8-4b15-4b3b-b1d3-f4f031eea2d6)

![12_DELETE2](https://github.com/JuangarcDev/Prueba_CRUD_DRF_PostGresql/assets/131199084/af348b3f-6a2b-4c9e-9234-cf7d908d791e)

Se puede apreciar como se elimina de la BD el registro de la película con id =2, posteriormente se intenta buscar con get, pero no se encunetra ningun registro con id = 2 ya que se elimino.













