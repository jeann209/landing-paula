from flask import Blueprint, render_template

main = Blueprint('main', __name__)

NAV_LINKS = [
    {"label": "Inicio", "href": "#inicio"},
    {"label": "Sobre mí", "href": "#sobre-mi"},
    {"label": "Servicios", "href": "#servicios"},
    {"label": "Testimonios", "href": "#testimonios"},
    {"label": "Contacto", "href": "#contacto"},
]

SERVICIOS = [
    {"nombre": "Ansiedad\ny estrés", "icono": "img/icon-brain.svg"},
    {"nombre": "Autoestima\ny desarrollo personal", "icono": "img/icon-heart.svg"},
    {"nombre": "Terapia de pareja", "icono": "img/icon-couple.svg"},
    {"nombre": "Gestión emocional", "icono": "img/icon-smile.svg"},
    {"nombre": "Duelo y procesos\nde vida", "icono": "img/icon-lotus.svg"},
    {"nombre": "Orientación\npara adolescentes", "icono": "img/icon-user.svg"},
]

TESTIMONIOS = [
    {
        "texto": "Gracias a Paula he aprendido a gestionar mi ansiedad y a ver la vida desde otra perspectiva. Es un apoyo invaluable.",
        "nombre": "María S.",
    },
    {
        "texto": "Su forma de escuchar y guiarme ha sido clave en mi proceso personal. Me siento muy cómoda en cada sesión.",
        "nombre": "Andrés G.",
    },
    {
        "texto": "Un espacio de confianza, respeto y profesionalismo. Totalmente recomendada.",
        "nombre": "Valentina R.",
    },
]

WHATSAPP_NUMERO = "573000000000"
WHATSAPP_MENSAJE = "Hola Paula, me gustaría agendar una cita."

EMAIL_CONTACTO = "atencion@paulavillarrealpsico.com"


@main.route('/')
def index():
    return render_template(
        'index.html',
        nav_links=NAV_LINKS,
        servicios=SERVICIOS,
        testimonios=TESTIMONIOS,
        whatsapp_numero=WHATSAPP_NUMERO,
        whatsapp_mensaje=WHATSAPP_MENSAJE,
        email_contacto=EMAIL_CONTACTO,
    )
