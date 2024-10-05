from django.http import HttpResponse

# HTTP -> HyperText Transfer Protocol

# Essa função chamamos de view. Uma view é responsável por retornar uma resposta http válida para o navegador. Podemos criar 2 tipos de views: As function-based-views (Views baseadas em função) e as class-based-views(Views baseadas em classe).
def index(request):
    return HttpResponse("Você está na página principal das enquetes.")

def detalhes(request, pergunta_id):
    return HttpResponse(f"Você está na página de detalhes da pergunta {pergunta_id}.")

def resultados(request, pergunta_id):
    return HttpResponse(f"Você está na página de resultados da pergunta {pergunta_id}.")

def votar(request, pergunta_id):
    return HttpResponse(f"Você está votando na pergunta {pergunta_id}.")
