"""
Laços de condição

Laço while

O laço while é utilizado quando precisamos executar um bloco de código repetidas vezes, enquanto uma determinada condição é verdadeira

container = estrutura que contém outros tipos de dados
iterável = estrutura em que é possível acessar os itens de maneira sequencial dentro de um loop

"""

from random import randint
from time import sleep

if __name__ == "__main__":

    """
    Dicionários são um outro tipo de estrutura de dados em Python, caracterizada pelo formato chave: valor. Como valor, podemos ter quaisquer outros tipos de dados (strings, numeros, listas, outros dicionarios, etc), porém como chaves podemos ter apenas os tipos básicos do python (strings, tipos numericos e booleanos)

    Dicionários são:
        Iteráveis;
        Indexáveis;
        Mutáveis;
    
    """
    
    heroi = {
        "nome": "Astolfus",
        "att": 8,
        "def": 15,
        "hp": 30
    }

    monstro = {
        "nome": "Orc",
        "att": 7,
        "def": 13,
        "hp": 20
    }

    batalha_ocorrendo = True
    vencedor = None

    while batalha_ocorrendo:
        
        print(f"{heroi['nome']} ataca {monstro['nome']}.")
        dado = randint(1, 12)

        ataque_heroi = heroi['att'] + dado
        if ataque_heroi > monstro['def']:
            monstro['hp'] = monstro['hp'] - (ataque_heroi - monstro['def'])

        else:
            print(f"{monstro['nome']} defendeu o ataque!")

        if monstro['hp'] <= 0:
            vencedor = heroi
            batalha_ocorrendo = False
            continue

        sleep(1)
        # =================================

        print(f"{monstro['nome']} ataca {heroi['nome']}.")
        dado = randint(1, 10)

        ataque_monstro = monstro['att'] + dado
        if ataque_monstro > heroi['def']:
            heroi['hp'] = heroi['hp'] - (ataque_monstro - heroi['def'])

        else:
            print(f"{heroi['nome']} defendeu o ataque!")

        if heroi['hp'] <= 0:
            vencedor = monstro
            batalha_ocorrendo = False
            continue

        print(heroi)
        print(monstro)

        sleep(1)

    print(f"Vencedor: {vencedor}")