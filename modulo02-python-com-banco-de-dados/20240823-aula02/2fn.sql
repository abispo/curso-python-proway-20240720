/*
Segunda Forma Normal (2FN)

A Segunda Forma Normal, exige que:
 * A tabela esteja na 1FN;
 * Não existam dependências parciais. Ou seja, todos as colunas não-chave da tabela devem
 * depender totalmente da chave primária. Chamamos isso de dependência funcional total
*/

USE formas_normais;

CREATE TABLE IF NOT EXISTS tb_cursos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	carga_horaria INT NOT NULL
);

INSERT INTO tb_cursos(nome, carga_horaria) VALUES
("Fundamentos de Python", 30),
("Java avançado", 50),
("Análise de dados com Python", 40);
INSERT INTO tb_cursos (nome, carga_horaria) VALUES
("PHP Básico", 20);
SELECT * FROM tb_cursos tc ;

CREATE TABLE IF NOT EXISTS curso_instrutor(
	curso_id INT NOT NULL,
	instrutor_id INT NOT NULL,
	nome_instrutor VARCHAR(100) NOT NULL,
	email_instrutor VARCHAR(100) NOT NULL,
	PRIMARY KEY(curso_id, instrutor_id),
	FOREIGN KEY(curso_id) REFERENCES tb_cursos(id)
);
INSERT INTO curso_instrutor (curso_id, instrutor_id, nome_instrutor, email_instrutor) VALUES
(1, 1, "José da Silva", "jose.silva@email.com"),
(2, 2, "Paulo Carvalho", "paulo.carvalho@email.com"),
(3, 3, "Márcia Luz", "marcia.luz@email.com");
SELECT * FROM curso_instrutor ci ;

INSERT INTO curso_instrutor (curso_id, instrutor_id, nome_instrutor, email_instrutor) VALUES
(1, 2, "Márcia Luz", "marcia@email.com");

/*
NO caso acima, AS colunas 'nome_instrutor' e 'email_instrutor' dependem apenas de uma parte da
chave primária (coluna instrutor_id), gerando assim uma dependência parcial. Para resolver isso,
vamos criar a tabela tb_instrutores
*/
DROP TABLE curso_instrutor ;

CREATE TABLE IF NOT EXISTS tb_instrutores(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL
);

INSERT INTO tb_instrutores(nome, email) VALUES
("José da Silva", "jose.silva@email.com"),
("Paulo Carvalho", "paulo.carvalho@email.com"),
("Márcia Luz", "marcia.luz@email.com");

CREATE TABLE IF NOT EXISTS tb_cursos_instrutores(
	curso_id INT NOT NULL,
	instrutor_id INT NOT NULL,
	PRIMARY KEY(curso_id, instrutor_id),
	FOREIGN KEY(curso_id) REFERENCES tb_cursos(id),
	FOREIGN KEY(instrutor_id) REFERENCES tb_instrutores(id)
);

INSERT INTO tb_cursos_instrutores(curso_id, instrutor_id) VALUES 
(1, 1),
(2, 2),
(3, 3),
(1, 3);

SELECT * FROM tb_cursos_instrutores;
INSERT INTO tb_instrutores(nome, email) VALUES ("Carlos Sá", "carlos.sa@email.com")

-- tb_cursos a
-- tb_cursos_instrutores b
-- tb_instrutores c


SELECT a.id AS curso_id, a.nome, a.carga_horaria, c.id AS instrutor_id, c.nome, c.email FROM tb_cursos a
INNER JOIN tb_cursos_instrutores b
ON a.id = b.curso_id
INNER JOIN tb_instrutores c
ON b.instrutor_id = c.id;

SELECT a.id AS curso_id, a.nome, a.carga_horaria, c.id AS instrutor_id, c.nome, c.email FROM tb_cursos a
INNER JOIN tb_cursos_instrutores b
ON a.id = b.curso_id
INNER JOIN tb_instrutores c
ON b.instrutor_id = c.id;