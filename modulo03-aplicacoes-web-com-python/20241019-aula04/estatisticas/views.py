from django.db.models import Count, Avg, Sum
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

    # O método annotate cria atributos nos objetos que estão sendo retornados do banco. No caso abaixo, para cada instância da model Pergunta, está sendo criado o atributo num_votos, que irá armazenar a quantidade de votos que as opções de cada pergunta tiveram.
    lista_de_perguntas_ordenada_pela_quantidade_de_votos = Pergunta.objects.annotate(
        num_votos=Sum("opcao__votos")
    ).order_by("-num_votos")[:5]

    return render(
        request,
        "estatisticas/index.html",
        context={
            "quantidade_de_perguntas_cadastradas": quantidade_de_perguntas_cadastradas,
            "quantidade_de_opcoes_cadastradas": quantidade_de_opcoes_cadastradas,
            "media_de_opcoes_por_pergunta": media_de_opcoes_por_pergunta,
            "lista_de_perguntas_ordenada_pela_quantidade_de_votos": lista_de_perguntas_ordenada_pela_quantidade_de_votos
        }
    )
