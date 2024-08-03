# 9. Escreva um programa em Python que gere uma lista randômica de 50 números de 1 até 50. Em seguida, retire os valores repetidos dessa lista (utilize a função randint() do pacote random)

from random import randint

if __name__ == "__main__":
    lista_randomicos = [randint(1, 50) for _ in range(50)]
    conjunto = set(lista_randomicos)
    lista_randomicos = list(conjunto)

    print(lista_randomicos)