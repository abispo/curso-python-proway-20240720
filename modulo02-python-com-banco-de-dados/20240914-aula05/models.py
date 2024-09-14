# módulo das models

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from config import Base

class Usuario(Base):

    __tablename__ = "tb_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    senha = Column(String(100), nullable=False)


class Perfil(Base):

    __tablename__ = "tb_perfis"

    id = Column(Integer, ForeignKey("tb_usuarios.id"), primary_key=True)
    nome = Column(String(100), nullable=False)
    sobrenome = Column(String(100), nullable=False)
    genero = Column(String(20), nullable=True)
    data_de_nascimento = Column(Date, nullable=True)
