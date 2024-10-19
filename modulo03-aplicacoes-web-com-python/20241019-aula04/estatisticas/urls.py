from django.urls import path

from . import views

"""
Como o django sabe que deve executar uma determinada view de acordo com a URL que é passada na chamado.

1 - Ele consulta o arquivo urls.py do projeto (meu_site.urls), verificando se o padrão que foi informado na URL existe em alguma chamada a função path. 

"""

app_name = "estatisticas"

urlpatterns = [
    path("", views.index, name="index"),
]
