/*
Terceira Forma Normal (3FN)

Uma tabela estará na Terceira Forma Normal, se:
	* Ela está na Segunda Forma Normal
	* Todos os campos não-chave da tabela não dependam de outros campos não chave. Essa dependência é
	* chamada de dependência transitiva
*/

USE formas_normais;

CREATE TABLE IF NOT EXISTS tb_itens(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	valor_unitario FLOAT NOT NULL
);
INSERT INTO tb_itens(nome, valor_unitario) VALUES
("Bandana do Restart", 9.90),
("Mochila do Naruto", 89.90),
("Camisa do Linkin Park", 59.90),
("All star colorido", 109.90),
("Calça rasgada", 129.90);

CREATE TABLE IF NOT EXISTS tb_pedidos(
	id INT PRIMARY KEY AUTO_INCREMENT,
	data_hora DATETIME NOT NULL,
	descricao VARCHAR(200) NULL
);
INSERT INTO tb_pedidos(data_hora, descricao) VALUES
("2024-01-21 12:45:54", NULL),
("2024-02-14 18:12:37", "Pedido especial"),
("2024-04-03 09:39:10", NULL);
SELECT * FROM tb_pedidos;

CREATE TABLE IF NOT EXISTS tb_pedidos_itens(
	pedido_id INT NOT NULL,
	item_id INT NOT NULL,
	quantidade INT NOT NULL,
	subtotal FLOAT NOT NULL,
	PRIMARY KEY (pedido_id, item_id),
	FOREIGN KEY (pedido_id) REFERENCES tb_pedidos(id),
	FOREIGN KEY (item_id) REFERENCES tb_itens(id)
);
SELECT * FROM tb_pedidos_itens ;

INSERT INTO tb_pedidos_itens(pedido_id, item_id, quantidade, subtotal) VALUES
(1, 1, 2, 19.80),
(1, 2, 1, 89.90),
(2, 2, 2, 179.80),
(3, 3, 3, 179.70),
(3, 4, 2, 217.80);

-- tb_pedidos a
-- tb_pedidos_itens b
-- tb_itens c

SELECT a.id, a.data_hora, c.nome, c.valor_unitario, b.quantidade, b.subtotal FROM tb_pedidos a
INNER JOIN tb_pedidos_itens b
ON a.id = b.pedido_id
INNER JOIN tb_itens c
ON c.id = b.item_id;

-- A coluna subtotal, que não é chave primária, depende de outras colunas que também não são chave,
-- que são as colunas 'valor_unitario' e 'quantidade'.
-- Solução: Remover a coluna subtotal e calcular esse valor em tempo de execução

ALTER TABLE tb_pedidos_itens DROP COLUMN subtotal;
DESC tb_pedidos_itens;

SELECT
a.id,
a.data_hora,
c.nome,
c.valor_unitario,
b.quantidade,
FORMAT(c.valor_unitario * b.quantidade, 2) AS "Subtotal" FROM tb_pedidos a
INNER JOIN tb_pedidos_itens b
ON a.id = b.pedido_id
INNER JOIN tb_itens c
ON c.id = b.item_id;
