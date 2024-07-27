# Exercício 1
# Crie um programa que peça ao usuário para digitar um número inteiro e exiba se ele é positivo, negativo ou zero.

def tipo_numero():
    numero = int(input("Informe um número inteiro: "))

    if numero < 0:
        print("O número é negativo.")

    elif numero > 0:
        print("O número é positivo.")

    else:
        print("O número é 0")


if __name__ == "__main__":

    tipo_numero()