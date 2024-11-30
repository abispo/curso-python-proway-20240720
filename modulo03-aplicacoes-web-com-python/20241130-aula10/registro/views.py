from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from . import forms
from .exceptions import PreRegistroInvalido, PreRegistroExpirado
from .models import PreRegistro, Perfil
from .utils import enviar_email
from .validators import todos_dados_foram_preenchidos, nome_de_usuario_ja_existe

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

            # Valida se já não existe um cadastro com esse e-mail
            email_ja_cadastrado = User.objects.filter(
                email=email
            )

            if email_valido_existe_no_pre_registro or email_ja_cadastrado:
                form.add_error(
                    "email", "O e-mail informado não é válido. Verifique se já possui cadastro no sistema ou se ainda não confirmou um pré-registro anterior."
                )

                return render(
                    request,
                    "registro/pre_registro.html",
                    {"form": form}
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
        try:

            token = request.GET.get("id")

            pre_registro_valido = PreRegistro.objects.filter(
                token=token, valido=True
            ).first()

            if not pre_registro_valido:
                rota_redirecionar = "registro:pre_registro_invalido"
                raise PreRegistroInvalido()
            
            pre_registro_expirado = (
                timezone.now() - pre_registro_valido.criado_em
            ).total_seconds() > settings.TEMPO_LIMITE_CONFIRMACAO_PRE_REGISTRO

            if pre_registro_expirado:
                pre_registro_valido.valido = False
                pre_registro_valido.save()
                rota_redirecionar = "registro:pre_registro_expirado"

                raise PreRegistroExpirado()

            return render(
                request,
                "registro/registro.html",
                {"pre_registro": pre_registro_valido}
            )
        
        except ValidationError:
            return redirect(reverse(rota_redirecionar))
    
    elif request.method == "POST":

        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        nome_de_usuario = request.POST.get("nome_de_usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmacao_de_senha = request.POST.get("confirmacao_de_senha")

        """
        Implementar as seguintes validações:
            1. Validar se todos os dados recebidos foram preenchidos
            2. Validar se o nome de usuário informado já não existe na tabela de usuários
            3. Validar se o valor de senha é igual ao valor de confirmacao_de_senha

        Implemente essas validações como funções. Essas funções devem ser criadas no arquivo validators.py, que se encontra no pacote registro. Elas devem ser importadas nesse módulo e chamadas antes da criação do usuário
        """

        pre_registro = PreRegistro.objects.filter(email=email).first()
        erros = []

        dados_preenchidos = todos_dados_foram_preenchidos(
            nome, sobrenome, nome_de_usuario, email, senha, confirmacao_de_senha
        )

        if not dados_preenchidos:
            erros.append("Você deve preencher todos os dados do formulário.")

        username_ja_existe = nome_de_usuario_ja_existe(
            nome_de_usuario
        )

        if username_ja_existe:
            erros.append(f"O nome de usuário '{nome_de_usuario}' já existe no cadastro. Escolha outro")

        if erros:
            return render(
                request,
                "registro/registro.html",
                {
                    "pre_registro": pre_registro,
                    "erros": erros
                }
            )

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

        pre_registro.valido = False
        pre_registro.save()

        return redirect(reverse("registro:confirmacao_cadastro"))

def confirmacao_cadastro(request: HttpRequest):
    return render(
        request,
        "registro/confirmacao_cadastro.html"
    )

def pre_registro_invalido(request):
    return render(
        request,
        "registro/pre_registro_invalido.html"
    )

def pre_registro_expirado(request):
    return render(
        request,
        "registro/pre_registro_expirado.html"
    )