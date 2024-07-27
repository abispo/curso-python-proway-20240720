"""
Laços de condição

Laço for

O laço for é geralmente utilizando quando precisamos percorrer uma estrutura de dados do tipo container, que será iterável.

container = estrutura que contém outros tipos de dados
iterável = estrutura em que é possível acessar os itens de maneira sequencial dentro de um loop

"""

# A função randint gera um numero aleatório dentro de um intervalo
from random import randint


if __name__ == "__main__":
    curso = "Python"

    for letra in curso:
        print(letra, end='-')

    # Podemos utilizar com outros tipos iteráveis, como listas, dicionários e tuplas
        
    # Digamos que temos uma lista de números, e queremos gerar uma outra lista com os quadrados desses números
    # Lista de entrada: [1, 2, 3, 4, 5, 6]
    # Lista de saída: [1, 4, 9, 16, 25, 36]
        
    lista_de_numeros = [1, 2, 3, 4, 5, 6]
    lista_de_numeros_ao_quadrado = []

    for numero in lista_de_numeros:
        lista_de_numeros_ao_quadrado.append(numero * numero)

    print(lista_de_numeros_ao_quadrado)
    print(lista_de_numeros_ao_quadrado[3])
    lista_de_numeros_ao_quadrado[0] = 0
    print(lista_de_numeros_ao_quadrado)

    """
    Listas em Python são estruturas de dados:
        iteráveis: Permitem a iteração através do comando for
        indexáveis: Permitem acessar um determinado valor a partir do índice
        mutáveis: Permitem que um determinado valor seja alterado diretamente utilizando o índice
    """

    lista_randomicos = []

    # Utilizando o método append
    for _ in range(1, 101):
        lista_randomicos.append(randint(1, 100))

    # Utilizando list-comprehension
    # O underline é utilizado quando não vamos precisar acessar o valor da variável que recebe os itens da sequencia
    lista_randomicos = [randint(1, 100) for _ in range(1, 101)]

    # lista_randomicos = list(set(lista_randomicos))

    # lista_randomicos.sort()

    for numero in lista_randomicos:

        if numero < 5 or numero > 96:
            print("Valores muito altos ou muito baixos")
            # O break interrompe imediatamente a execução do laço for, independentemente se existirem mais itens a serem lidos na lista
            break


    for numero in lista_randomicos:
        if numero >= 5 and numero <= 96:
            # O continue ignora o restante do código dentro do laço for e volta ao começo, para continuar a iteração
            continue

        print("Valores muito altos ou muito baixos")
        break

    lista = [1, 1, 0, 1, 1]

    for resultado in lista:
        if resultado == 0:
            print("Nem todos os resultados obtiveram êxito.")
            break

    # Caso o comando break não tenha sido executado dentro do laço for, o código do bloco else é executado
    else:
        print("Todos os resultados com êxito.")