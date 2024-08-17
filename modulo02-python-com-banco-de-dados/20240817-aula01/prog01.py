"""
Python com banco de dados.

Assim como diversas outras linguagens, podemos utilizar o Python para trabalhar com banco de dados. Geralmente utilizamos uma biblioteca para fazer isso.

No caso do Python, por padrão, ele já vem com uma biblioteca para trabalharmos com bancos de dados SQLite.
"""

import json
import os

# 1. Importamos a biblioteca de conexão com o banco
import sqlite3

if __name__ == "__main__":
    """
    Para trabalharmos com qualquer banco de dados, geralmente seguimos esses passos:

    1. Importamos a biblioteca de conexão com o banco
    2. Criamos uma connection string (string de conexão)
    3. Abrimos uma conexão com o banco de dados utilizando a connection string
    4. Criamos um cursor que será utilizado para enviar comandos SQL ao banco de dados
    5. Manipulamos os dados (consulta, inserção, atualização, etc)
    6. Fechamos a conexão com o banco de dados
    """

    # 2. Criamos uma connection string
    connection_string = os.path.join(os.getcwd(), "db.sqlite3")

    # 3. Abrimos uma conexão com o banco de dados
    connection = sqlite3.connect(connection_string)

    # 4. Criamos um cursor a partir da conexão
    cursor = connection.cursor()

    # 5. Manipulação dos dados
    comando = "DROP TABLE IF EXISTS tb_estados"
    cursor.execute(comando)

    comando = """
CREATE TABLE tb_estados(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sigla TEXT NOT NULL
);
"""
    cursor.execute(comando)

    with open("estados.json", mode="r", encoding="utf-8") as arquivo:
        data = json.load(arquivo)

    estados = data.get("UF")

    for estado in estados:
        comando = "INSERT INTO tb_estados(nome, sigla) VALUES('{}', '{}');".format(
            estado.get("nome"), estado.get("sigla")
        )
        cursor.execute(comando)
    
    connection.commit()

    # 6. Fechamos a conexão com o banco de dados
    connection.close()
