
from config import Base, connection
from mensagens import MENU_GERAL
from models import Usuario, Perfil

if __name__ == "__main__":
    Base.metadata.create_all(connection)

    while True:
        print(MENU_GERAL)
        opcao = int(input("Informe a opção: "))

        match opcao:
            case 0:
                print("Saindo...")
                break