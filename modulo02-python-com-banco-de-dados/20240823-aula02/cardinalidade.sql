/*
Cardinalidade

Em um banco de dados relacional, existem níveis de relacionamento entre AS tabelas.
Chamamos esses níveis de cardinalidade. Existem 3 níveis de relacionamento que
2 tabelas podem ter entre si:

1:1 - Um para Um
1:N - Um para Muitos
N:N - Muitos para Muitos

Para ilustrar, vamos criar uma estrutura simples simulando a base de dados de um
blog.

Nesse exemplo, vamos ter algumas entidades que precisaremos armazenar os valores.
São elas:
	- Usuario
	- Perfil
	- Postagem
	- Comentario
	- Categoria
*/

-- Relação 1:1 - Quando, no relacionamento entre tabelas, existe uma, e somente uma
-- referência da tabela pai na tabela filha.
-- Exemplo: Um usuário pode ter apenas um Perfil associado a ele, e vice-versa

CREATE TABLE IF NOT EXISTS tb_usuarios(
	id INT PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(200) NOT NULL,
	senha VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_perfis(
	id INT PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	sobrenome VARCHAR(200) NOT NULL,
	genero VARCHAR(20) NULL,
	data_de_nascimento DATE NULL,
	FOREIGN KEY (id) REFERENCES tb_usuarios(id)
);

INSERT INTO tb_usuarios (email, senha) VALUES
("jose@email.com", "123456"),
("maria@email.com", "123456"),
("carla@email.com", "123456");

INSERT INTO tb_perfis (id, nome, sobrenome, genero, data_de_nascimento) VALUES
(1, "José", "da Silva", "masculino", "1979-11-07"),
(2, "Maria", "das Graças", "feminino", "1993-04-07"),
(3, "Carla", "dos Reis", "feminino", "1998-01-05");

SELECT * FROM tb_perfis ;

-- Acima, garantimos que, na tabela tb_perfis, haverá apenas uma correspondência de um registro a
-- tabela tb_clientes. Ou seja, uma linha na tabela tb_perfis estará associada a apenas uma linha
-- na tabela tb_clientes, e vice-versa.

-- Relação 1:N. Quando, em uma tabela filha, existem zero, uma ou mais correspondências de um registro
-- que está na tabela pai. Ou seja, uma linha na tabela pai, tem zero, uma ou mais linhas associadas
-- na tabela filha
-- Exemplo: Criação da tabela de postagens

CREATE TABLE IF NOT EXISTS tb_postagens(
	id INT PRIMARY KEY AUTO_INCREMENT,
	perfil_id INT NOT NULL,
	titulo VARCHAR(100) NOT NULL,
	texto TEXT NOT NULL,
	data_hora DATETIME NOT NULL,
	FOREIGN KEY (perfil_id) REFERENCES tb_perfis(id)
);

INSERT INTO tb_postagens (perfil_id, titulo, texto, data_hora) VALUES
(1, "A Linguagem Python", "Python é legal", NOW()),
(1, "A linguagem Java", "Java é poderoso", "2024-07-14 13:25:43"),
(2, "Devops: Uma Introdução", "Devops é infraestrutura como código.", "2024-08-11 19:15:02");
SELECT * FROM tb_postagens ;

--

CREATE TABLE IF NOT EXISTS tb_categorias(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL
);
DESC tb_categorias ;
INSERT INTO tb_categorias (nome) VALUES
	("TI"),
	("Programação"),
	("Python"),
	("Java"),
	("Linux");
SELECT * FROM tb_categorias ;

-- Como temos uma relação de N:N entre as tabelas tb_postagens e tb_categorias, precisamos
-- criar uma tabela que fará a ligação entre esses registros, chamada de tabela associativa.

CREATE TABLE IF NOT EXISTS tb_postagens_categorias(
	postagem_id INT NOT NULL,
	categoria_id INT NOT NULL,
	PRIMARY KEY(postagem_id, categoria_id),
	FOREIGN KEY(postagem_id) REFERENCES tb_postagens(id),
	FOREIGN KEY(categoria_id) REFERENCES tb_categorias(id)
);
DESC tb_postagens_categorias;
-- Associando as categorias "TI", "Programação" e "Python", a postagem de título "A Linguagem Python"
INSERT INTO tb_postagens_categorias (postagem_id, categoria_id) VALUES
	(1, 1),
	(1, 2),
	(1, 3);
SELECT * FROM tb_postagens_categorias ;

-- tb_postagens a
-- tb_postagens_categorias b
-- tb_categorias c

SELECT a.id, a.titulo, c.nome FROM tb_postagens a
INNER JOIN tb_postagens_categorias b
ON a.id = b.postagem_id
INNER JOIN tb_categorias c
ON b.categoria_id = c.id
WHERE a.id = 1;

-- Com o comando acima, conseguimos saber quais categorias estão associadas
-- a postagem "A Linguagem Python"