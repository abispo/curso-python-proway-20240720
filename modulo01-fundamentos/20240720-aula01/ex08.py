# Crie um programa que receba um número inteiro e exiba se ele é par ou ímpar.

if __name__ == "__main__":

    numero = int(input("Informe o número: "))

    # Operador resto da divisão (%)
    if numero % 2 == 0:
        print("O número é par.")

    else:
        print("O número é ímpar.")
