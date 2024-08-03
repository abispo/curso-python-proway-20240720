"""
Funções (Procedures)

Funções são blocos de código que podem ser ser chamados em qualquer lugar do nosso programa. As funções podem receber valores a partir de parâmetros e também retornar valores. Funções também são consideradas objetos dentro do Python.

Para criar uma função, utilizamos a palavra reservada def.
"""

from datetime import datetime

# Função sem parametros e sem retorno
def ola():
    print("Olá Python")

# Função sem parametros e com retorno
def hora_certa():
    return datetime.now()

# Função com parâmetros e com retorno
def calculo_imc(altura, peso):
    return peso / (altura * altura)

# Função com parâmetros opcionais e retorno
# IMPORTANTE! Os parâmetros opcionais devem sempre vir obrigatoriamente após os parâmetros obrigatórios
def calculo_ganhos(valor, multiplicador, adicional=0):
    return (valor * multiplicador) + adicional

if __name__ == "__main__":

    # Exemplo 1: Função sem parâmetros e que não retorna valor
    print(ola())

    # Exemplo 2: Função sem parâmetros retornando valor
    print(hora_certa())

    # Exemplo 3
    print(f"Altura: 1.66 | Peso: 80 | IMC: {calculo_imc(1.66, 80):.2f}.")

    # Se quisermos, podemos informar explicitamente para qual parâmetro está indo determinado valor. Nesse caso, não precisamos respeitar a ordem dos parâmetros.
    print(f"Altura: 2.10 | Peso: 111.50 | IMC: {calculo_imc(peso=111.50, altura=2.10):.2f}.")

    # Podemos utilizar um recurso bem interessante de funções, chamado desempacotamento de parametros
    lista_para_imc = [
        [1.67, 65.7], [1.74, 101.3], [1.99, 80], [1.55, 45.9], [1.71, 110.2]
    ]

    for peso_altura in lista_para_imc:
        altura = peso_altura[0]
        peso = peso_altura[1]
        print(f"Altura: {altura} | Peso: {peso} | IMC: {calculo_imc(*peso_altura):.2f}.")

    # No caso acima, utilizamos o desempacotamento usando listas de valores. Cada valor será atribuído a um parâmetro, respeitando a posição. Ou seja, o valor no índice 0 da lista será passada para o primeiro parâmetro, o valor do índice 1 será passado para o segundo parâmetro, e assim em diante.

    print('-'*50)

    # Utilizando desempacotamento com dicionários

    lista_para_imc = [
        {
            "peso": 81.3,
            "altura": 1.78
        },
        {
            "peso": 98.1,
            "altura": 1.83
        },
        {
            "peso": 75.7,
            "altura": 1.88
        }
    ]

    for dado in lista_para_imc:
        altura = dado["altura"]
        peso = dado["peso"]

        print(f"Altura: {altura} | Peso: {peso} | IMC: {calculo_imc(**dado):.2f}.")

    print('-'*50)

    print(calculo_ganhos(300, 1.3))
    print(calculo_ganhos(500, 1.7, 100))
    print(calculo_ganhos(multiplicador=2.2, valor=60, adicional=200))
