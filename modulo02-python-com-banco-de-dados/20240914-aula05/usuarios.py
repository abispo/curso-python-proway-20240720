
from config import session
from mensagens import MENU_USUARIOS
from models import Usuario, Perfil

def gerenciar_usuarios():
    
    while True:
        print(MENU_USUARIOS)
        opcao = int(input("Informe a opção: "))

        match opcao:
            case 0:
                print("Saindo...")
                break

            case 1:
                usuarios = listar_usuarios()

                if len(usuarios) == 0:
                    print("Não existem usuários cadastrados.")

                for usuario in usuarios:
                    print(usuario)

def listar_usuarios():
    return session.query(Usuario).all()

def cadastrar_usuario(
        email: str,
        senha: str,
        nome: str,
        sobrenome: str,
        data_de_nascimento: str,
        genero: str | None = None
    ):
    usuario = Usuario(
        email=email,
        senha=senha
    )

    