
import csv
import sqlite3

if __name__ == "__main__":

    connection_string = "db.sqlite3"
    connection = sqlite3.connect(connection_string)
    cursor = connection.cursor()

    comando = "DROP TABLE IF EXISTS tb_cursos;"
    cursor.execute(comando)

    comando = """
        CREATE TABLE IF NOT EXISTS tb_cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            curso TEXT NOT NULL,
            carga_horaria INTEGER NOT NULL,
            preco REAL not null
        );
"""
    cursor.execute(comando)
    
    with open("cursos.csv", "r", encoding="utf-8") as arquivo:

        arquivo_csv = csv.DictReader(arquivo, delimiter=';')

        for linha in arquivo_csv:
            comando = "INSERT INTO tb_cursos(curso, carga_horaria, preco) VALUES ('{}', {}, {});".format(
                linha.get("curso"),
                int(linha.get("carga_horaria")),
                float(linha.get("preco"))
            )
            cursor.execute(comando)

        connection.commit()

    # 1º método
    comando = "SELECT * FROM tb_cursos"
    result = cursor.execute(comando).fetchall()

    qtd_cursos = len(result)
    curso_maior_carga_horaria = sorted(result, key=lambda item: item[2], reverse=True)[0]
    curso_com_maior_valor = sorted(result, key=lambda item: item[3], reverse=True)[0]

    print(f"Quantidade de cursos: {qtd_cursos}")
    print("Curso com a maior carga horária: {} ({}hs)".format(
        curso_maior_carga_horaria[1],
        curso_maior_carga_horaria[2]
    ))
    print("Curso com o maior valor: {} ({}hs)".format(
        curso_com_maior_valor[1],
        curso_com_maior_valor[3]
    ))

    print('*'*50)

    # 2º Método
    comando = "SELECT COUNT(id) FROM tb_cursos;"
    result = cursor.execute(comando).fetchone()
    qtd_cursos = result[0]
    print(f"Quantidade de cursos: {qtd_cursos}")

    comando = "SELECT * FROM tb_cursos ORDER BY carga_horaria DESC;"
    curso_maior_carga_horaria = cursor.execute(comando).fetchone()
    print("Curso com a maior carga horária: {} ({}hs)".format(
        curso_maior_carga_horaria[1],
        curso_maior_carga_horaria[2]
    ))

    comando = "SELECT * FROM tb_cursos ORDER BY preco DESC;"
    curso_com_maior_valor = cursor.execute(comando).fetchone()
    print("Curso com o maior preço: {} ({}hs)".format(
        curso_com_maior_valor[1],
        curso_com_maior_valor[3]
    ))

    cursor.close()
    connection.close()
