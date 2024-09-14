
from config import session
from mensagens import MENU_USUARIOS, MENSAGEM_LISTA_USUARIO
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
                    print(MENSAGEM_LISTA_USUARIO.format(
                        nome=usuario.perfil.nome,
                        sobrenome=usuario.perfil.sobrenome,
                        email=usuario.email,
                        data_de_nascimento=usuario.perfil.data_de_nascimento
                    ))
                    print('*'*50)

            case 2:
                email = input("Informe o e-mail do novo usuário: ")
                senha = input("Informe a senha do novo usuário: ")
                nome = input("Informe o nome do novo usuário: ")
                sobrenome = input("Informe o sobrenome do novo usuário: ")
                data_de_nascimento = input("Informe a data de nascimento do novo usuário (formato yyyy-mm-dd): ")
                genero = input("Informe o gênero do novo usuário: ")

                cadastrar_usuario(
                    email=email, senha=senha, nome=nome, sobrenome=sobrenome,
                    data_de_nascimento=data_de_nascimento, genero=genero
                )

                print("Usuário cadastrado com sucesso.")

def listar_usuarios():
    return session.query(Usuario).all()

def cadastrar_usuario(
        email: str,
        senha: str,
        nome: str,
        sobrenome: str,
        data_de_nascimento: str,
        genero: str = ""
    ):
    usuario = Usuario(
        email=email,
        senha=senha
    )

    session.add(usuario)
    session.commit()

    cadastrar_perfil(
        usuario_id=usuario.id,
        nome=nome,
        sobrenome=sobrenome,
        data_de_nascimento=data_de_nascimento,
        genero=genero
    )

def cadastrar_perfil(
        usuario_id: int,
        nome: str,
        sobrenome: str,
        data_de_nascimento: str,
        genero: str
    ):
    
    perfil = Perfil(
        id=usuario_id,
        nome=nome,
        sobrenome=sobrenome,
        data_de_nascimento=data_de_nascimento
    )

    if genero:
        perfil.genero = genero

    session.add(perfil)
    session.commit()