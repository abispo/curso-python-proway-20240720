import datetime

from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    texto = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField("Data de publicação")

    # Dentro de uma model, podemos alterar as configurações padrão dela declarando a classe Meta. No exemplo abaixo, alteramos o nome padrão que o Django daria para a tabela para tb_perguntas

    def __str__(self) -> str:
        return "({}) {}".format(
            self.id, self.texto
        )
    
    def publicado_recentemente(self) -> bool:
        return self.data_publicacao >= timezone.now() - datetime.timedelta(days=1) # 04/10/2024

    class Meta:
        db_table = "tb_perguntas"


class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self) -> str:
        return "{} ({})".format(
            self.texto, self.pergunta.texto
        )

    class Meta:
        db_table = "tb_opcoes"