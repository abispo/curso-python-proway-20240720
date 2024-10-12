from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Pergunta

# HTTP -> HyperText Transfer Protocol

# Essa função chamamos de view. Uma view é responsável por retornar uma resposta http válida para o navegador. Podemos criar 2 tipos de views: As function-based-views (Views baseadas em função) e as class-based-views(Views baseadas em classe).
def index(request):
    # SELECT * FROM tb_perguntas ORDER BY data_publicacao DESC
    lista_perguntas = Pergunta.objects.order_by(
        "-data_publicacao"
    )

    context = {
        "lista_perguntas": lista_perguntas,
    }

    return render(request, "enquetes/index.html", context)

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

    return render(
        request,
        "enquetes/detalhes.html",
        context={"pergunta": pergunta}
    )

def resultados(request, pergunta_id):
    return HttpResponse(f"Você está na página de resultados da pergunta {pergunta_id}.")

def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando na pergunta {pergunta_id}.")
