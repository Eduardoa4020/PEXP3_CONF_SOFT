# PEXP3_CONF_SOFT

Aplicación web de gestión de tareas desarrollada con Django y PostgreSQL.
El proyecto incluye configuración Docker Compose y un flujo de integración
continua con GitHub Actions para ejecutar migraciones, pruebas y construir la
imagen Docker.

## Requisitos

- Docker Desktop con Docker Compose.
- Git, para clonar el repositorio.

## Iniciar la aplicación con Docker

Clona el repositorio y entra a su carpeta:

```powershell
git clone https://github.com/Eduardoa4020/PEXP3_CONF_SOFT.git
cd PEXP3_CONF_SOFT
```

Construye y arranca los contenedores:

```powershell
docker compose up --build -d
```

Aplica las migraciones de Django a la base PostgreSQL:

```powershell
docker compose exec web python manage.py migrate --noinput
```

Abre [http://localhost:8000](http://localhost:8000) para usar la aplicación.
Para revisar los servicios y sus puertos:

```powershell
docker compose ps
```

Al terminar, detén los contenedores:

```powershell
docker compose down
```

## Pruebas

Con los servicios Docker activos y la base inicializada, ejecuta:

```powershell
docker compose exec web python manage.py test
```

El workflow `.github/workflows/ci.yml` también aplica migraciones y ejecuta
las pruebas en GitHub Actions. Después construye la imagen Docker, la guarda
como `django-app.tar.gz` y la publica como el artefacto `django-app-image`.

## Despliegue simulado

Consulta [deploy-notes.md](deploy-notes.md) para los pasos y resultados de la
prueba del artefacto de GitHub Actions en una carpeta externa.
