from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


class PreRegistro(models.Model):
    email = models.CharField("E-mail", max_length=100)
    token = models.UUIDField(default=uuid4)
    criado_em = models.DateTimeField(auto_now_add=True)
    valido = models.BooleanField(default=True)

    class Meta:
        db_table = "tb_pre_registro"


class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    documento = models.CharField(max_length=20, null=True, blank=True)
    genero = models.CharField(max_length=30, null=True, blank=True)
    data_de_nascimento = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return "{} {} ({})".format(
            self.usuario.first_name,
            self.usuario.last_name,
            self.usuario.email
        )
    
    class Meta:
        db_table = "tb_perfis"