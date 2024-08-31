"""
Programação Orientada a Objetos em Python

Classes, Métodos, Atributos e Objetos
"""

class Pokemon:
    def __init__(self, nome: str, tipo: str, hp: int) -> None:
        self._nome = nome
        self._tipo = tipo
        self._hp = hp

    def get_nome(self):
        return self._nome
    
    def get_tipo(self):
        return self._tipo
    
    def set_tipo(self, novo_tipo):
        self._tipo = novo_tipo

    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, novo_hp):
        self._hp = novo_hp

    def atacar(self):
        print(f"{self._nome} atacou!")

    def desviar(self):
        print(f"{self._nome} desviou!")

    def evoluir(self):
        print(f"{self._nome} evoluiu!")

if __name__ == "__main__":
    pass
