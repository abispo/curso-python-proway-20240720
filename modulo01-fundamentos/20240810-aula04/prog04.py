"""
Trabalhando com arquivos .csv em Python

Escrevendo em arquivos .csv com writer e DictWriter

"""

import csv
import os
import uuid

if __name__ == "__main__":

    caminho_arquivo = os.path.join(os.getcwd(), "arquivos", "compras.csv")

    lista_itens = [
        [str(uuid.uuid4()), "Abacaxi", 2, 9.90],
        [str(uuid.uuid4()), "Laranja", 1, 4.50],
        [str(uuid.uuid4()), "Morango", 2, 11],
        [str(uuid.uuid4()), "Alface", 3, 5],
        [str(uuid.uuid4()), "Pimenta", 1, 3.50]
    ]

    with open(caminho_arquivo, "w", encoding="utf-8", newline="") as arquivo:
        
        arquivo_csv = csv.writer(arquivo, delimiter=';')

        # O método writerow recebe uma lista de valores, que serão salvos no arquivo. Cada item da lista será separado pelo delimitador
        arquivo_csv.writerow(["id", "nome", "quantidade", "valor_unitario"])

        # O método writerows recebe uma lista de listas. Cada item dessa lista de listas será salvo como uma linha, e os itens dessa linha serão separados pelo delimitador
        arquivo_csv.writerows(lista_itens)

# ---------------------------

    caminho_arquivo = os.path.join(os.getcwd(), "arquivos", "funcionarios.csv")

    with open(caminho_arquivo, "w", encoding="utf-8", newline="") as arquivo:

        lista_funcionarios = [
            {"nome": "Ugo", "setor": 3},
            {"nome": "Samantha", "setor": 1},
            {"nome": "Rogério", "setor": 3},
        ]

        # Aqui usamos o parâmetro fieldnames, que indica os nomes das colunas do arquivo
        arquivo_csv = csv.DictWriter(arquivo, delimiter=';', fieldnames=["nome", "setor"])

        # Aqui salvamos os nomes das colunas
        arquivo_csv.writeheader()

        # Aqui salvamos os dados no arquivo
        arquivo_csv.writerow({"nome": "Ivan", "setor": 2})

        # Aqui salvamos os dados no arquivo que estão na lista
        arquivo_csv.writerows(lista_funcionarios)