from django.http import HttpResponse

# HTTP -> HyperText Transfer Protocol

# Essa função chamamos de view. Uma view é responsável por retornar uma resposta http válida para o navegador. Podemos criar 2 tipos de views: As function-based-views (Views baseadas em função) e as class-based-views(Views baseadas em classe).
def index(request):
    return HttpResponse("Você está na página principal das enquetes.")
