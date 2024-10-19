from django.db.models import Count, Avg
from django.shortcuts import render

from enquetes.models import Pergunta, Opcao

def index(request):

    # O método count() retorna a quantidade de registros existentes na tabela associada a model Pergunta
    quantidade_de_perguntas_cadastradas = Pergunta.objects.count()
    quantidade_de_opcoes_cadastradas = Opcao.objects.count()
    media_de_opcoes_por_pergunta = quantidade_de_opcoes_cadastradas / quantidade_de_perguntas_cadastradas
    # media_de_opcoes_por_pergunta = Pergunta.objects.annotate(
    #     numero_de_opcoes=Count("opcao")
    # ).aggregate(media_opcoes=Avg("numero_de_opcoes"))["media_opcoes"]

    return render(
        request,
        "estatisticas/index.html",
        context={
            "quantidade_de_perguntas_cadastradas": quantidade_de_perguntas_cadastradas,
            "quantidade_de_opcoes_cadastradas": quantidade_de_opcoes_cadastradas,
            "media_de_opcoes_por_pergunta": media_de_opcoes_por_pergunta
        }
    )
