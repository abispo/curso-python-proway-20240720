# Acesso a banco de dados utilizando o ORM SQLAlchemy

SQLAlchemy é um ORM (Object Relational Mapper | Mapeador Objeto Relacional). Basicamente utilizamos para trabalhar com banco de dados utilizando orientação a objetos.

## Alembic
Alembic é uma ferramente de migração de banco de dados utilizada geralmente junto com o SQLAlchemy. Uma ferramenta de migração permite que tenhamos um histórico de alterações no nosso banco de dados, além de permitir uma rápida configuração das nossas tabelas via código (`code-first`).

### Instalação e configuração do alembic
`(NÃO ESQUEÇA DE CRIAR UM VIRTUALENV PARA O SEU PROJETO)`
Para instalarmos o alembic, rodamos o comando `pip install alembic`. Depois de instalado, geramos os arquivos de configuração com o comando `alembic init alembic`. Esse comando irá criar na raiz do projeto o arquivo `alembic.ini`, e uma pasta chamada `alembic`, com outras configurações, inclusive o script de carregamento.

Após uma configuração inicial, geralmente seguimos esse passo-a-passo para se trabalhar com a ferramenta:

1. Fazer as alterações que precisamos nas models
2. Rodar o comando `alembic revision --autogenerate -m "<mensagem>"` para gerar o arquivo de migration, que por padrão será salvo na pasta `alembic/versions`
3. Fazemos uma rápida revisão dos comandos que foram gerados nesse arquivo.
4. Aplicamos a migração no banco de dados com o comando `alembic revision head`, sendo o `head` um apelido para a última revision gerada.