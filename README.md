# Psicología Web

Landing page inicial (ejercicio "Answer the questions") construida con Flask, siguiendo la misma estructura de proyecto que [Gym-web](../Gym-web).

## Estructura

```
psicología/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── backend/
│   ├── __init__.py
│   ├── config.py
│   ├── main/            # blueprint de la landing
│   ├── static/
│   │   ├── css/styles.css
│   │   └── img/         # iconos SVG generados
│   └── templates/
│       ├── base.html
│       └── index.html
```

## Ejecutar con Docker

```bash
docker compose up --build
```

La app queda disponible en http://localhost:5031

## Ejecutar en local (sin Docker)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Próximos pasos

- Módulo de reservas: solicitar citas/reservas.
- Autenticación de usuario para ver su calendario de reservas.
