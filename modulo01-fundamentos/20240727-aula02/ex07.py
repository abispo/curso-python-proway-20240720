"""
7. Escreva um programa que receba nome, idade e sexo de 5 usuários. Em seguida, mostre quantos usuários são do sexo masculino, quantos são do sexo feminino e qual é a média de idade. Exemplo:

Nome: João
Idade: 32
Sexo: M

Nome: Maria
Idade: 17
Sexo: F

Nome: Vanessa
Idade: 28
Sexo: F

Quantidade de usuários do sexo masculino: 1
Quantidade de usuários do sexo feminino: 2
Média de idade: 25.67
"""

if __name__ == "__main__":
    qtd_masculino = 0
    qtd_feminino = 0
    soma_idade = 0
    media_de_idade = 0
    lista_usuarios = []

    qtd_usuarios = 5

    for _ in range(qtd_usuarios):

        nome = input("Informe o seu nome: ")
        if len(nome) <= 3 or not nome.isalpha():
            print("Informe um nome válido. ")
            break
        
        idade = int(input("Informe a sua idade: "))
        if idade <= 0:
            print("Informe uma idade válida.")
            break

        sexo = input("Informe o seu sexo (M ou F): ").upper()
        if sexo not in ["M", "F"]:
            print("Você deve informar 'M' ou 'F' para sexo.")
            break

        soma_idade = soma_idade + idade
        if sexo == "M":
            qtd_masculino += 1  # qtd_masculino = qtd_masculino + 1

        else:
            qtd_feminino += 1

        lista_usuarios.append({
            "nome": nome,
            "idade": idade,
            "sexo": sexo
        })

        print('-'*50)

    else:
        media_de_idade = soma_idade / qtd_usuarios

        for usuario in lista_usuarios:
            print(f"Nome: {usuario['nome']}")
            print(f"Idade: {usuario['idade']}")
            print(f"Sexo: {usuario['sexo']}")
            print()

        print(f"Quantidade de usuários do sexo masculino: {qtd_masculino}")
        print(f"Quantidade de usuários do sexo feminino: {qtd_feminino}")
        print(f"Média de idade: {media_de_idade:.2f}")
