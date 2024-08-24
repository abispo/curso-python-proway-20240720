
USE formas_normais;

/*
 * Primeira Forma Normal (1FN)
 * 
 * A Primeira Forma Normal define que cada coluna da tabela deve ter apenas valores atômicos ou
 * indivisíveis. Exige também que exista ao menos uma coluna da tabela que seja chave primária. Também
 * exige que não podemos ter colunas multivaloradas
 * 
 */

CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT,
	nome VARCHAR(200),
	endereco VARCHAR(200),
	telefone VARCHAR(50)
);

INSERT INTO tb_clientes (id, nome, endereco, telefone) VALUES
(1, "João da Silva", "Rua XV de Novembro, 1000, Centro, Blumenau, SC", "47923458923"),
(2, "Neide Carvalho", "Praça da Liberdade, 12, Liberdade, São Paulo, SP", "1194634563,11934581293"),
(2, "Maria Souza", "Rua dos Bandeirantes, 240, Centro, Pomerode, SC", "47988876123");
 

/*
 * A tabela 'tb_clientes' não atenda à 1FN, pois:
 * As colunas 'nome' e 'endereco' podem ser quebradas em outras colunas (não são dados indivisíveis)
 * A tabela 'tb_clientes' não possui chave primária
 * A coluna 'telefone' possui registros multivalorados (mais de 1 telefone por registro)
 */

RENAME TABLE tb_clientes TO tb_clientes_pre_1fn;

-- Vamos criar a tabela tb_clientes, aplicando as regras da 1FN
CREATE TABLE IF NOT EXISTS tb_clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(20) NOT NULL,
	sobrenome VARCHAR(50) NOT NULL,
	tipo_logradouro VARCHAR(20) NOT NULL,
	logradouro VARCHAR(100) NOT NULL,
	numero VARCHAR(10) NOT NULL,
	bairro VARCHAR(20) NOT NULL,
	cidade VARCHAR(50) NOT NULL,
	estado CHAR(2) NOT NULL
);

-- Como a coluna 'telefone' pode possuir mais de 1 valor, nesse caso vamos criar
-- a tabela 'tb_telefones', que terá uma chave estrangeira pra tabela 'tb_clientes'
CREATE TABLE IF NOT EXISTS tb_telefones(
	id INT PRIMARY KEY AUTO_INCREMENT,
	cliente_id INT NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	FOREIGN KEY(cliente_id) REFERENCES tb_clientes(id)
);

INSERT INTO tb_clientes (
	nome,
	sobrenome,
	tipo_logradouro,
	logradouro,
	numero,
	bairro,
	cidade,
	estado
) VALUES
("João", "da Silva", "Rua", "XV de Novembro", "1000", "Centro", "Blumenau", "SC"),
("Neide", "Carvalho", "Praça", "da Liberdade", "12", "Liberdade", "São Paulo", "SP"),
("Maria", "Souza", "Rua", "dos Bandeirantes", "240", "Centro", "Pomerode", "SC");

SELECT * FROM tb_clientes tc ;

-- Preencher os dados da tabela de telefones

INSERT INTO tb_telefones(cliente_id, telefone) VALUES
(1, "47988341413"),
(2, "47955647321"),
(2, "11987346110"),
(3, "47921217654");
SELECT * FROM tb_telefones;

-- tb_clientes a
-- tb_telefones b

INSERT INTO tb_clientes (
	nome,
	sobrenome,
	tipo_logradouro,
	logradouro,
	numero,
	bairro,
	cidade,
	estado
) VALUES
("José", "Bento", "Rua", "XV de Novembro", "1000", "Centro", "Blumenau", "SC");

SELECT a.nome, b.telefone FROM tb_clientes a
INNER JOIN tb_telefones b
ON a.id = b.cliente_id;

/*
Agora temos a tabela tb_clientes respeitando AS regras para ser considerada uma tabela que está na
1FN:
	- Aplicamos a chave primária
	- "Quebramos" AS colunas compostas em colunas simples
	- Criamos uma outra tabela que irá armazenar os telefones dos clientes, acabando assim com AS
colunas multivaloradas.
*/