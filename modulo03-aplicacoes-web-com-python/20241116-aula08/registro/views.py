from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from . import forms
from .models import PreRegistro
from .utils import enviar_email

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

            enviar_email(request, pre_registro)

            return redirect(reverse(
                "registro:envio_email_pre_registro"
            ))


def envio_email_pre_registro(request):
    return render(request, "registro/envio_email_pre_registro.html")


def registro(request: HttpRequest):
    token = request.GET.get("id")

    pre_registro_valido = PreRegistro.objects.filter(
        token=token, valido=True
    ).first()

    return render(
        request,
        "registro/registro.html",
        {"pre_registro": pre_registro_valido}
    )