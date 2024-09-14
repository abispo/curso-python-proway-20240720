# módulo das models

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config import Base

class Usuario(Base):

    __tablename__ = "tb_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    senha = Column(String(100), nullable=False)

    # Caso as tabelas que estão mapeadas estejam relacionadas, podemos criar uma relação no nível de objetos. Ou seja, o atributo 'perfil' irá conter o objeto usuário do registro relacionado na tabela.
    # O parâmetro back_populates indica qual será o atributo de ligação na outra classe
    # O parâmetro uselist serve para indicar se deve ser retornado apenas um objeto ou uma lista de objetos relacionados. No caso desse relacionamento (1:1), não faz sentido trazermos uma lista de usuários associados a esse perfil, pois o valor será sempre 1
    perfil = relationship("Perfil", back_populates="usuario", uselist=False)


class Perfil(Base):

    __tablename__ = "tb_perfis"

    id = Column(Integer, ForeignKey("tb_usuarios.id"), primary_key=True)
    nome = Column(String(100), nullable=False)
    sobrenome = Column(String(100), nullable=False)
    genero = Column(String(20), nullable=True)
    data_de_nascimento = Column(Date, nullable=True)

    usuario = relationship("Usuario", back_populates="perfil", uselist=False)
