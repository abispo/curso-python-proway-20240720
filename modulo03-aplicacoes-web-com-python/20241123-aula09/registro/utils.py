from django.core.mail import send_mail
from django.http.request import HttpRequest
from django.urls import reverse

from .models import PreRegistro

def enviar_email(request: HttpRequest, pre_registro: PreRegistro):
    mensagem_email = """
Você recebeu esse e-mail pois você ou alguém o cadastrou no sistema de gestão de imóveis.
Caso queira confirmar o cadastro, clique no link abaixo.
Caso não tenha sido você que realizou o pré-registro, apenas ignore esse e-mail.

{}{}{}?id={}
""".format(
    'https://' if request.is_secure() else 'http://',
    request.get_host(),
    reverse('registro:registro'),
    pre_registro.token
)
    send_mail(
        subject="Confirmação de pré-registro",
        message=mensagem_email,
        from_email="admin@localhost",
        recipient_list=[pre_registro.email]
    )