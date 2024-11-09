from django.shortcuts import render, redirect
from django.urls import reverse

from . import forms
from .models import PreRegistro

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
            
            email = form.cleaned_data["email"]

            pre_registro = PreRegistro(email=email)
            pre_registro.save()

            return redirect(reverse(
                "login"
            ))
