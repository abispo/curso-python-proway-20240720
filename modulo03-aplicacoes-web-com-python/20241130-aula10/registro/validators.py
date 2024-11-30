from django.contrib.auth.models import User

def todos_dados_foram_preenchidos(*args):
    return all(args)

def nome_de_usuario_ja_existe(nome_de_usuario: str):
    return bool(
        User.objects.filter(username=nome_de_usuario).first()
    )

def senhas_iguais(senha: str, confirmacao_de_senha: str):
    return senha == confirmacao_de_senha
