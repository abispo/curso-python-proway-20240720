# Escreva um programa que leia três números inteiros e exiba o maior e o menor deles.

if __name__ == "__main__":

    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))
    numero3 = int(input("Informe o terceiro número: "))

    # maior = 0

    # if numero1 >= numero2 and numero1 >= numero3:
    #     maior = numero1

    # elif numero2 >= numero1 and numero2 >= numero3:
    #     maior = numero2

    # elif numero3 >= numero1 and numero3 >= numero2:
    #     maior = numero3

    maior = max(numero1, numero2, numero3)
    menor = min(numero1, numero2, numero3)

    print(f"O maior número é o número {maior}")
    print(f"O menor número é o número {menor}")