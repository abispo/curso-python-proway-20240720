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

"""
Desafio: Criar a model Postagem, que será mapeada para a tabela tb_postagens. Os atributos e relacionamentos dessa model devem ser os mesmos que foram definidos na aula sobre cardinalidade (aula 2 | https://github.com/abispo/curso-python-proway-20240720/blob/main/modulo02-python-com-banco-de-dados/20240823-aula02/cardinalidade.sql)

Além dos relacionamentos, você deve criar os atributos do tipo relationship, de maneira semelhante como foi feito entre Usuario e Perfil. Ou seja, você vai criar a estrutura de um relacionamento 1:N, entre Perfil e Postagem. O objeto 'perfil' deve ter um atributo de nome 'postagens', que irá retornar a lista de posts feitos por determinado perfil, e o objeto 'postagem' terá um atributo chamado 'autor' que será o objeto perfil relacionado.

Desafio Bonus: Crie o relacionamento N:N entre Postagem e Categoria.
"""