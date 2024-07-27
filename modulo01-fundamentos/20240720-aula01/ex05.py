# Escreva um programa que solicite o nome, a idade e o sexo do usuário. Em seguida, exiba uma mensagem personalizada informando se o usuário é homem ou mulher e se é maior ou menor de idade.

if __name__ == "__main__":
    nome = input("Informe o seu nome: ")
    idade = int(input("Informe a sua idade: "))
    sexo = input("Informe o seu sexo (Informe M ou F): ")

    if idade < 18:
        maior_de_idade = False

    else:
        maior_de_idade = True

    saida = f"""
Nome: {nome}
{'Você é maior de idade' if maior_de_idade else 'Você é menor de idade'}
{'Você é do sexo masculino' if sexo.upper() == 'M' else 'Você é do sexo feminino'}
"""
    
    print(saida)