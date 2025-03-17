# Django / React App

# Enunciado
Elaborar el deployment dockerizado de una aplicación en django (backend) con frontend en React.js contenida en el repositorio. Es necesario desplegar todos los servicios
en un solo docker-compose.

Se deben entregar los Dockerfiles pertinentes para elaborar el despliegue y justificar la forma en la que elabora el deployment (supervisor, scripts, docker-compose, kubernetes, etc)

Subir todo lo elaborado a un repositorio (github, gitlab, bitbucket, etc). En el repositorio se debe incluir el código de la aplicación y un archivo README.md con instrucciones detalladas para compilar y desplegar la aplicación, tanto en una PC local como en la nube (AWS o GCP).


# Instrucciones

```bash
git clone https://github.com/jerebenitez/craftech-challenge-2025
cd django-react-app
cp .env.example .env # Modify this file!
docker compose up -d
```

You should be able to access Nginx Proxy Manager on port 81 to configure the domains. The frontend is accessed through port 3000, the backend through port 8000.

# Resolución
## 1. Correr backend en dev

El primer paso fue correr el back a mano, en development. Al principio se presentaron problemas a la hora de instalar psycopg2, que se solucionaron haciendo:

```bash
sudo apt install python3-dev libpq-dev
pip3 install psycopg2-binary
```

> Estos problemas reaparecieron luego a la hora de generar el `Dockerfile`, y fueron solucionados de la misma forma.

El segundo problema que se presentó, fue que `manage.py` no leía correctamente el archivo .env que se creara. Para lograrlo se tiene que correr:

```bash
env $(cat .env | xargs) python3 manage.py runserver
```

Con esto resuelto, se pudo correr el servidor haciendo

```bash
env $(cat .env | xargs) ./entrypoint.sh
```

Cabe aclarar que al `.env` se le tuvieron que agregar las siguientes variables:

```.env
SQL_HOST=localhost
SQL_PORT=5432
```

## 2. Correr frontend en dev

No presentó ningún problema. Se levantó con:

```bash
npm install
npm start
```

## 3. Correr back en producción

Basado en:
- [https://www.docker.com/blog/how-to-dockerize-react-app/]

> Se modificó el `Dockerfile` para reducir la cantidad de layers y agregar los paquetes necesarios.
> Se modificó `requirements.py` para agregar gunicorn y psycopg2-binary
> Se modificó `entrypoint.sh` para correr `python manage.py runserver` en development y `gunicorn` en prod. 

## 4. Correr front en producción

Basado en:
- [https://www.docker.com/blog/how-to-dockerize-django-app/]

> Se modificó levemente el `Dockerfile` para reducir el número de layers


## 5. Correr todo desde un compose.yml

El `compose.yml` levanta una db (en caso de ser necesaria, si se usa una db externa se puede eliminar ese servicio), así como los servicios del frontend y el backend, haciendo uso de los `Dockerfile`s creados anteriormente. Se agregó además una instancia de `nginx-proxy-manager` para manejar los dominios, el cual fue elegido frente a un ngnix "solo" por una mayor facilidad de uso, y porque configura automáticamente los certificados de ssl.
