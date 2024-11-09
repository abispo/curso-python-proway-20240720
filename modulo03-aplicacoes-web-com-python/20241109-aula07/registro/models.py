from uuid import uuid4
from django.db import models


class PreRegistro(models.Model):
    email = models.CharField("E-mail", max_length=100)
    token = models.UUIDField(default=uuid4)
    criado_em = models.DateTimeField(auto_now_add=True)
    valido = models.BooleanField(default=True)

    class Meta:
        db_table = "tb_pre_registro"