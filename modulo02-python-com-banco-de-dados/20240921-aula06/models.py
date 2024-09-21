# módulo das models

from sqlalchemy import func
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship
from config import Base

# Como temos uma relação N:N entre postagens e categorias, precisamos criar a tabela associativa que terá as chaves estrangeiras dessas tabelas. Abaixo criamos a tabela tb_postagens_categorias utilizando a classe Table
postagens_categorias = Table(
    "tb_postagens_categorias",
    Base.metadata,
    Column("postagem_id", Integer, ForeignKey("tb_postagens.id"), primary_key=True),
    Column("categoria_id", Integer, ForeignKey("tb_categorias.id"), primary_key=True)
)

class Usuario(Base):

    __tablename__ = "tb_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    senha = Column(String(100), nullable=False)
    criado_em = Column(DateTime, server_default=func.now())
    atualizado_em = Column(DateTime, onupdate=func.now())


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

    # Por padrão, o valor do parâmetro 'uselist' é igual a 'True'
    postagens = relationship("Postagem", back_populates="autor")
    usuario = relationship("Usuario", back_populates="perfil", uselist=False)


class Postagem(Base):

    __tablename__ = "tb_postagens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    perfil_id = Column(Integer, ForeignKey("tb_perfis.id"), nullable=False)
    titulo = Column(String(200), nullable=False)
    texto = Column(Text, nullable=False)
    data_hora = Column(DateTime, server_default=func.now())

    autor = relationship("Perfil", back_populates="postagens", uselist=False)
    # Como a relação entre Postagem e Categoria é uma relação de muitos para muitos (N:N), precisamos indicar o valor do parâmetro 'secondary' como sendo o objeto que representa a tabela associativa 'tb_postagens_categorias'
    categorias = relationship(
        "Categoria",
        secondary=postagens_categorias,
        back_populates="postagens"
    )


class Categoria(Base):

    __tablename__ = "tb_categorias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    postagens = relationship(
        "Postagem",
        secondary=postagens_categorias,
        back_populates="categorias"
    )
