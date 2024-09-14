# Aqui vamos configurar os objetos para trabalhar com SQLAlchemy

import os

# O pacote python-dotenv serve para carregar valores a partir de arquivos .env e definí-los como variáveis de ambiente. Muito útil quando não queremos expor quaisquer tipos de credenciais de acesso no nosso código
from dotenv import load_dotenv

# A função create_engine é responsável por criar a conexão com o banco de dados
from sqlalchemy import create_engine

# A função sessionmaker é responsável por criar a sessão de acesso ao banco, ou seja, é a partir do objeto criado a partir dessa função que vamos manipular as tabelas do banco de dados
from sqlalchemy.orm import sessionmaker