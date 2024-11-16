from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from . import forms
from .models import PreRegistro, Perfil
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

            # Valida se já não existe um pré-registro válido para esse e-mail
            email_valido_existe_no_pre_registro = PreRegistro.objects.filter(
                email=email, valido=True
            )

            pre_registro = PreRegistro(email=email)
            pre_registro.save()

            enviar_email(request, pre_registro)

            return redirect(reverse(
                "registro:envio_email_pre_registro"
            ))


def envio_email_pre_registro(request):
    return render(request, "registro/envio_email_pre_registro.html")


def registro(request: HttpRequest):

    if request.method == "GET":
        token = request.GET.get("id")

        pre_registro_valido = PreRegistro.objects.filter(
            token=token, valido=True
        ).first()

        return render(
            request,
            "registro/registro.html",
            {"pre_registro": pre_registro_valido}
        )
    
    elif request.method == "POST":

        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        nome_de_usuario = request.POST.get("nome_de_usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmacao_de_senha = request.POST.get("confirmacao_de_senha")

        usuario = User.objects.create_user(
            first_name=nome,
            last_name=sobrenome,
            username=nome_de_usuario,
            email=email,
            password=senha
        )

        Perfil.objects.create(
            usuario=usuario
        )

        return redirect(reverse("registro:confirmacao_cadastro"))

def confirmacao_cadastro(request: HttpRequest):
    return render(
        request,
        "registro/confirmacao_cadastro.html"
    )
