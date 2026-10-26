# Notas del despliegue simulado

## Objetivo

Validar el despliegue local de la aplicación Django desde una copia externa al
proyecto de desarrollo, usando la imagen Docker generada y publicada como
artefacto por GitHub Actions.

## Repositorio y artefacto

- Repositorio: [PEXP3_CONF_SOFT](https://github.com/Eduardoa4020/PEXP3_CONF_SOFT)
- Workflow: [Django CI, ejecución 11](https://github.com/Eduardoa4020/PEXP3_CONF_SOFT/actions/runs/40251477955)
- Resultado del workflow: exitoso.
- Nombre del artefacto: `django-app-image`
- Archivo dentro del artefacto descargado: `django-app.tar.gz`
- Imagen Docker cargada: `django-app:latest`
- Fecha de la prueba: 25 de octubre de 2026.

## Requisitos

- Docker Desktop iniciado.
- Git instalado.
- Acceso al repositorio de GitHub.
- Descargar el artefacto `django-app-image` desde la ejecución exitosa del
  workflow y extraer el ZIP.
- Copiar `django-app.tar.gz` a la carpeta externa del proyecto.

## Procedimiento

### 1. Clonar el repositorio en una carpeta externa

La prueba se realizó en `Desktop\despliegue-simulacion`, separado de la carpeta
original del proyecto:

```powershell
cd $HOME\Desktop
git clone https://github.com/Eduardoa4020/PEXP3_CONF_SOFT.git despliegue-simulacion
cd $HOME\Desktop\despliegue-simulacion
```

### 2. Cargar la imagen generada por Actions

Se copió el archivo descargado a la raíz de la copia externa y se cargó en
Docker:

```powershell
Copy-Item "$HOME\Downloads\django-app.tar.gz" .
docker load -i .\django-app.tar.gz
```

Docker confirmó la carga con el mensaje:

```text
Loaded image: django-app:latest
```

### 3. Iniciar los servicios con la imagen cargada

En el primer intento, el puerto `5432` ya estaba ocupado por PostgreSQL del
proyecto original. Se detuvieron los servicios de esa instancia y se limpió el
intento fallido en la copia externa. Después se inició Compose sin reconstruir
la imagen:

```powershell
docker compose down
docker compose up -d --no-build
docker compose ps
```

La configuración de Compose usa `django-app:latest` para el servicio web y
PostgreSQL 14 para la base de datos. La opción `--no-build` evita reconstruir
localmente la imagen descargada desde Actions.

### 4. Aplicar las migraciones

La primera visita a la página indicó que aún no existía la tabla `app_task` en
la base de datos nueva. Se inicializó el esquema ejecutando:

```powershell
docker compose exec web python manage.py migrate --noinput
```

Las migraciones de Django, incluidas las de la aplicación, se aplicaron
correctamente.

### 5. Verificar el despliegue

Se comprobó el estado de los contenedores:

```powershell
docker compose ps
```

Resultado observado:

- `despliegue-simulacion-db-1`: activo y `healthy`.
- `despliegue-simulacion-web-1`: activo (`Up`).
- Puerto de Django: `localhost:8000`.
- Puerto de PostgreSQL: `localhost:5432`.

Finalmente se abrió [http://localhost:8000](http://localhost:8000) en el
navegador. La aplicación mostró la página **“Mis tareas”** correctamente.

## Resultados

El despliegue simulado fue satisfactorio: la imagen del artefacto se cargó sin
reconstrucción, Compose inició Django y PostgreSQL en la carpeta externa, las
migraciones inicializaron la base de datos y la interfaz de tareas quedó
accesible en el navegador.

## Evidencias

Adjuntar al informe final las capturas tomadas durante la prueba:

1. Terminal con `docker load`, `docker compose ps` y los estados de los
   contenedores.
2. Terminal con la ejecución de `python manage.py migrate --noinput` y sus
   migraciones exitosas.
3. Navegador en `http://localhost:8000` mostrando la página de tareas.
4. Ejecución de GitHub Actions con el workflow exitoso y el artefacto
   `django-app-image`.

## Detener el despliegue

Al terminar la validación, los servicios se pueden detener desde la carpeta
externa con:

```powershell
docker compose down
```
