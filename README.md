# Portafolio Retro

Portafolio personal desarrollado con Django, con una interfaz visual inspirada en videojuegos retro. El sitio presenta informacion profesional, proyectos destacados, habilidades tecnicas y un formulario de contacto dentro de una experiencia bilingue y con cambios de tema.

## Demo

Puedes desplegar este proyecto en Vercel o ejecutarlo localmente con Django.

## Caracteristicas

- Interfaz retro con modo `gaming` y modo `normal`
- Cambio de idioma entre espanol e ingles
- Seccion de proyectos con filtros por categoria
- Seccion de habilidades tecnicas
- Formulario de contacto con mensaje de confirmacion en la interfaz
- Archivos estaticos servidos con WhiteNoise
- Configuracion lista para despliegue en Vercel

## Tecnologias

- Python
- Django
- HTML
- CSS
- JavaScript
- WhiteNoise
- Vercel

## Estructura del proyecto

```text
PortafolioRetro/
|-- portfolio/
|   |-- static/
|   |-- templates/
|   |-- urls.py
|   `-- views.py
|-- pt_retro/
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- manage.py
|-- requirements.txt
`-- vercel.json
```

## Instalacion local

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/PortafolioRetro.git
cd PortafolioRetro
```

2. Crea y activa un entorno virtual:

```bash
python -m venv env
```

En Windows:

```bash
env\Scripts\activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecuta el servidor:

```bash
python manage.py runserver
```

5. Abre en el navegador:

```text
http://127.0.0.1:8000/
```

## Despliegue en Vercel

Este proyecto ya incluye un archivo `vercel.json` para enrutar la aplicacion Django y publicar los archivos estaticos.

Pasos generales:

1. Sube el proyecto a GitHub.
2. Importa el repositorio en Vercel.
3. Vercel instalara dependencias y ejecutara:

```bash
python manage.py collectstatic --noinput
```

4. Publica el proyecto.

## Nota sobre el formulario

Actualmente el formulario de contacto:

- recibe `name`, `email` y `message`
- muestra un mensaje de exito en pantalla
- imprime el contenido en consola del servidor

No envia correos ni guarda la informacion en una base de datos persistente. Si se despliega en Vercel, ese comportamiento sigue funcionando visualmente, pero no reemplaza un sistema real de contacto.

## Personalizacion

Puedes modificar facilmente:

- la informacion personal desde la plantilla principal
- los proyectos mostrados en `portfolio/templates/portafolio/main.html`
- los estilos en `portfolio/static/portafolio/main.css`
- la logica de la vista principal en `portfolio/views.py`

## Estado del proyecto

Proyecto funcional orientado a presentacion personal y despliegue web rapido.

## Autor

Kevin Yepes

- GitHub: https://github.com/KeviinYepes
- LinkedIn: https://www.linkedin.com/in/keviinyepes
