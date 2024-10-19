from django.shortcuts import render

from enquetes.models import Pergunta, Opcao

def index(request):

    # O método count() retorna a quantidade de registros existentes na tabela associada a model Pergunta
    quantidade_de_perguntas_cadastradas = Pergunta.objects.count()
    quantidade_de_opcoes_cadastradas = Opcao.objects.count()

    return render(
        request,
        "estatisticas/index.html",
        context={
            "quantidade_de_perguntas_cadastradas": quantidade_de_perguntas_cadastradas,
            "quantidade_de_opcoes_cadastradas": quantidade_de_opcoes_cadastradas
        }
    )
