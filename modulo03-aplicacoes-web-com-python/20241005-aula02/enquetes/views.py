from django.http import HttpResponse

from .models import Pergunta

# HTTP -> HyperText Transfer Protocol

# Essa função chamamos de view. Uma view é responsável por retornar uma resposta http válida para o navegador. Podemos criar 2 tipos de views: As function-based-views (Views baseadas em função) e as class-based-views(Views baseadas em classe).
def index(request):
    lista_perguntas = Pergunta.objects.order_by(
        "-data_publicacao"
    )

    saida = ", ".join([pergunta.texto for pergunta in lista_perguntas])
    return HttpResponse(saida)

def detalhes(request, pergunta_id):
    return HttpResponse(f"Você está na página de detalhes da pergunta {pergunta_id}.")

def resultados(request, pergunta_id):
    return HttpResponse(f"Você está na página de resultados da pergunta {pergunta_id}.")

def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando na pergunta {pergunta_id}.")
