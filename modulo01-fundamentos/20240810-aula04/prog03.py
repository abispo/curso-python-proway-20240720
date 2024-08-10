"""
Trabalhando com arquivos .csv em Python

Lendo arquivos .csv com reader e DictReader

"""

import csv
import os

if __name__ == "__main__":

    # Aqui utilizamos as funções da linguagem para indicar o caminho do arquivo. os.getcwd() retorna o caminho completo de onde o script está sendo executa. os.path.join concatena caminhos do sistema.
    caminho_arquivo = os.path.join(os.getcwd(), "arquivos", "clientes.csv")

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:

        # Aqui utizamos a função reader do módulo csv. Com a função reader, trabalhamos com o conteúdo do arquivo sendo uma lista de listas, com cada coluna do arquivo sendo um item da lista
        # Como as colunas do nosso arquivo estão separadas por ponto-e-vírgula, precisamos indicar isso pelo parâmetro delimiter
        arquivo_csv = csv.reader(arquivo, delimiter=';')

        for linha in arquivo_csv:
            print(linha)
