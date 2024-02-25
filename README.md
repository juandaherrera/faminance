# 👋🏻 Bienvenido a Faminance

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.0.2-5646ED?style=for-the-badge&logo=django&logoColor=white&labelColor=101010)](https://reflex.dev)

[![Django CI](https://github.com/juandaherrera/faminance/actions/workflows/django.yml/badge.svg)](https://github.com/juandaherrera/faminance/actions/workflows/django.yml)

## Descripción

Faminance es una herramienta diseñada para gestionar las finanzas de toda una familia de manera eficiente y sencilla. Este proyecto busca facilitar el seguimiento de ingresos, gastos, y ahorros familiares, promoviendo una mejor organización financiera.

## Instalación

Para instalar Faminance, sigue los siguientes pasos:

### Requisitos previos

Asegúrate de tener Python 3.11 o superior instalado en tu sistema. Puedes descargarlo desde [Python.org](https://python.org).

### Configuración del entorno virtual

1. Clona el repositorio de Faminance a tu máquina local:
    ```bash
    git clone https://tu-repositorio-aqui.git
    ```
2. Accede al directorio del proyecto:
    ```bash
    cd faminance
    ```
3. Crea un entorno virtual:
    ```bash
    python3 -m venv .venv
    ```
4. Activa el entorno virtual:
   - En Windows:
        ```bash
        .\venv\Scripts\activate
        ```
   - En Unix o MacOS:
        ```bash
        source venv/bin/activate
        ```

### Instalación de dependencias
Faminance tiene dos archivos de requisitos: `requirements.txt` para producción y `dev-requirements.txt` para desarrollo.

- Para instalar las dependencias de producción:
  ```bash
  pip install -r requirements.txt
  ```
- Para entornos de desarrollo:
    ```bash
    pip install -r dev-requirements.txt
    ```

## Configuración

### Variables de entorno
Para configurar el entorno de desarrollo adecuadamente, debes crear un archivo `.env` en la raíz del proyecto. Este archivo debe contener las siguientes variables de entorno, que son esenciales para la configuración del proyecto:

```plaintext
# Ambiente de Django ('development' para desarrollo, 'production' para producción)
DJANGO_ENV=development

# Clave secreta de Django, genera una usando 'django.core.management.utils.get_random_secret_key()'
DJANGO_SECRET_KEY=...

# Debug encendido / apagado
DJANGO_DEBUG=True
```

En el repositorio se incluye un [ejemplo](.env.example) de cómo debería verse este archivo.


## Licencia
Este proyecto está bajo la Licencia GNU Affero General Public License v3.0 - vea el archivo [LICENSE](LICENSE) para más detalles.