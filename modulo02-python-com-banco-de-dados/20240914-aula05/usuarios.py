
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

def listar_usuarios():
    return session.query(Usuario).all()
