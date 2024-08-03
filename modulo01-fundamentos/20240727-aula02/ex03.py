# 3. Escreva um programa que gere 100 números randômicos de 1 a 100. Em seguida, crie 2 listas: Uma que irá salvar apenas os números pares, e outra que irá salvar apenas os números ímpares. Em seguida, mostre na tela a quantidade de itens de cada lista e quais são os seus valores.

from random import randint

if __name__ == "__main__":

    numeros_pares = []
    numeros_impares = []

    for _ in range(100):
        
        numero_randomico = randint(1, 100)

        if numero_randomico % 2 == 0:
            numeros_pares.append(numero_randomico)

        else:
            numeros_impares.append(numero_randomico)

    print(f"Lista de números pares: {numeros_pares}.")
    print(f"Tamanho: {len(numeros_pares)}.")
    print('*'*30)
    print(f"Lista de números ímpares: {numeros_impares}.")
    print(f"Tamanho: {len(numeros_impares)}.")