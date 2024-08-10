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