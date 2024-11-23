from django.urls import path

from . import views

app_name = "registro"

urlpatterns = [
    path("", views.registro, name="registro"),
    path("pre-registro/", views.pre_registro, name="pre_registro"),
    path(
        "envio-email-pre-registro/",
        views.envio_email_pre_registro,
        name="envio_email_pre_registro"
    ),
    path("confirmacao-cadastro/", views.confirmacao_cadastro, name="confirmacao_cadastro"),
    path("pre-registro-invalido/", views.pre_registro_invalido, name="pre_registro_invalido")
]
