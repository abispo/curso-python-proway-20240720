
from mensagens import MENU_GERAL
from usuarios import gerenciar_usuarios

if __name__ == "__main__":

    while True:
        print(MENU_GERAL)
        opcao = int(input("Informe a opção: "))

        match opcao:
            case 0:
                print("Saindo...")
                break

            case 1:
                gerenciar_usuarios()

            case 2 | 3:
                print("Ainda não foi implementado")

            case _:
                print(f"Opção '{opcao}' desconhecida.")