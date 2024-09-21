import requests

from mensagens import MENU_POKEMONS

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/{}"

if __name__ == "__main__":
    
    while True:
        print(MENU_POKEMONS)
        opcao = int(input("Informe a opção: "))

        match opcao:
            case 0:
                print("Saindo...")
                break

            case 1: # Opção que irá acessar o banco e listar os dados
                pass

            case 2: # Opção que irá acessar a API, baixar os dados e salvar nas tabelas
                pokemon = input("Informe o nome do pokémon a ser cadastrado: ")
                resposta = requests.get(
                    POKEAPI_URL.format(pokemon.lower())
                )
                
                if resposta.status_code == 404:
                    print(f"Pokémon '{pokemon}' não encontrado.")
                
                elif resposta.status_code == 200:
                    dados = resposta.json()
                    print(dados)

                else:
                    print(f"Não foi possível encontrar o pokémon '{pokemon}': {resposta.reason}")

            #Opção que irá apagar os dados do pokémon da tabela
            case 3:
                pass

            case _:
                print(f"Opção '{opcao}' desconhecida.")