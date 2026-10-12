# Landing — Paula Villarreal, Psicóloga

Landing page construida con Flask (hero, servicios, sobre mí, testimonios y contacto),
lista para correr en Docker.

## Estructura

```
psicología/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── env-example.txt
├── backend/
│   ├── __init__.py
│   ├── config.py
│   ├── main/            # blueprint de la landing
│   ├── static/
│   │   ├── css/styles.css
│   │   └── img/         # logo, fondos e iconos
│   └── templates/
│       ├── base.html
│       └── index.html
```

## Desplegar en un servidor

Requisitos: `git`, `docker` y el plugin `docker compose`.

```bash
git clone https://github.com/jeann209/landing-paula.git
cd landing-paula
docker compose up -d --build
```

La página queda en `http://IP_DEL_SERVIDOR:5031`

Comandos útiles:

```bash
docker compose logs -f      # ver logs
docker compose restart      # reiniciar
docker compose down         # detener
```

### Actualizar a la última versión

```bash
git pull
docker compose up -d --build
```

### Servir en el puerto 80

Editar el mapeo en `docker-compose.yml`:

```yaml
ports:
  - 80:5000/tcp
```

## Ejecutar en local (sin Docker)

```bash
python -m venv venv
venv\Scripts\activate        # Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Configuración

| Dónde | Qué |
|---|---|
| `.env` | `SECRET_KEY`, `DEBUG` |
| `backend/main/routes.py` | número de WhatsApp, correo de contacto, servicios y testimonios |

## Próximos pasos

- Módulo de reservas: solicitar citas.
- Autenticación de usuario para ver su calendario de reservas.
