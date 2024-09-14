# Aqui vamos configurar os objetos para trabalhar com SQLAlchemy

import os

# O pacote python-dotenv serve para carregar valores a partir de arquivos .env e definí-los como variáveis de ambiente. Muito útil quando não queremos expor quaisquer tipos de credenciais de acesso no nosso código
from dotenv import load_dotenv

# A função create_engine é responsável por criar a conexão com o banco de dados
from sqlalchemy import create_engine

# A função sessionmaker é responsável por criar a sessão de acesso ao banco, ou seja, é a partir do objeto criado a partir dessa função que vamos manipular as tabelas do banco de dados
from sqlalchemy.orm import sessionmaker

# A partir da função declarative_base, nós vamos criar a classe que será herdada por todas as models do nosso sistema. Model é uma classe comum, porém que está mapeada para uma tabela no banco de dados.
from sqlalchemy.ext.declarative import declarative_base

# A função load_dotenv carrega as informações a partir de um arquivo .env e as transforma em variáveis de ambiente.
load_dotenv()

# Aqui carregou os dados do arquivo .env
connection_string = os.getenv("CONNECTION_STRING")

# Aqui criamos o objeto de conexão ao banco de dados. O parâmetro echo serve para indicar se queremos que os comandos SQL executados sejam exibidos no terminal
connection = create_engine(url=connection_string, echo=True)

# Aqui criamos o objeto sessão, ligando ele a conexão criada anteriormente
Session = sessionmaker(bind=connection)
session = Session()

# Base é a classe que será herdada por todas as models do projeto.
Base = declarative_base()
