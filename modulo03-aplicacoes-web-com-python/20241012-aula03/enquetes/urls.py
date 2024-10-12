from django.urls import path

from . import views

"""
Como o django sabe que deve executar uma determinada view de acordo com a URL que é passada na chamado.

1 - Ele consulta o arquivo urls.py do projeto (meu_site.urls), verificando se o padrão que foi informado na URL existe em alguma chamada a função path. 

"""

app_name = "enquetes"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pergunta_id>/", views.detalhes, name="detalhes"),
    path("<int:pergunta_id>/resultados/", views.resultados, name="resultados"),
    path("<int:pergunta_id>/votar/", views.votar, name="votar"),
]
