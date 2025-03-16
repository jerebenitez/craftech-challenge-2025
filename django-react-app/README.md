# Django / React App

# Enunciado

# Resolución
## 1. Correr backend en dev

El primer paso fue correr el back en development. Al principio se presentaron problemas a la hora de instalar psycopg2, que se solucionaron haciendo:

```bash
sudo apt install python3-dev libpq-dev
pip3 install psycopg2
```

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

## 4. Correr front en producción

Basado en:
- [https://www.docker.com/blog/how-to-dockerize-django-app/]


## 5. Correr todo desde un compose.yml


