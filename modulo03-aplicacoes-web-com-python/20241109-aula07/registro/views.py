from django.shortcuts import render

from . import forms

def pre_registro(request):

    if request.method == "GET":
        form = forms.PreRegistroForm()

        return render(
            request,
            "registro/pre_registro.html",
            {"form": form}
        )
    
    elif request.method == "POST":
        
        # Automaticamente preenche os atributos da classe PreRegistroForm com o que está vindo no método POST
        form = forms.PreRegistroForm(request.POST)

        # Verifica se o formulário enviado é válido:
        if form.is_valid():
            pass
