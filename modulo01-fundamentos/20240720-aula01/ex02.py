# 2. Escreva um programa que receba a idade de uma pessoa e verifique se ela é menor de idade (menor que 18 anos) ou maior de idade.

if __name__ == "__main__":

    idade = int(input("Informe a sua idade: "))

    if idade < 18:
        print("Você não atingiu a maioridade.")

    else:
        print("Você já atingiu a maioridade.")
