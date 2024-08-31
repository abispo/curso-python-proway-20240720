"""
Programação Orientada a Objetos em Python

Classes, Métodos, Atributos e Objetos
"""

# PascalCase    -> FuncionarioTerceirizado
# camelCase     -> gerarReceita()
# snake_case    -> gerar_relatorio()
# UPPER_CASE    -> BIT = 1

class Pokemon:
    # O método __init__ é o método inicializador da classe, ou seja, nesse método criamos os atributos da classe e também podemos chamar os métodos. No caso abaixo, o método __init__ irá receber 3 valores: nome, tipo, hp
    # No caso dos métodos em uma classe Python, o primeiro parâmetro deve ser obrigatoriamente o self, pois é uma referência ao próprio objeto instanciado.
    def __init__(self, nome: str, tipo: str, hp: int) -> None:
        # Abaixo estamos inicializando 3 atributos: _nome, _tipo e _hp. Como no Python não existe uma palavra reservada que faça um atributo ser privado, os atributos que queremos que sejam entendidos como privados criamos com um underline na frente.
        # Abaixo os atributos estão recebendo os valores passados na criação do objeto
        self._nome = nome
        self._tipo = tipo
        self._hp = hp   # vitalidade

    def get_nome(self):
        # Obrigatoriamente, todos os métodos dentro de uma classe Python devem receber no mínimo o parâmetro self, que é uma referência ao próprio objeto que está sendo criado. Você pode verificar isso utilizando o método built-in id. Por exemplo: id(self) e depois passando o objeto criado para o método: id(pikachu)
        # Caso o método seja do tipo classmethod ou staticmethod, nós não passamos o parâmetro self
        return self._nome
    
    def get_tipo(self):
        return self._tipo
    
    def set_tipo(self, novo_tipo):
        self._tipo = novo_tipo

    # Abaixo utilizamos o decorator property (decorators são funções que extendem o comportamento de outras funções). Nesse caso, o método hp vai se comportar como uma propriedade hp. Ou seja, ao invés de fazermos objeto.hp(), fazemos objeto.hp.
    @property
    def hp(self):
        return self._hp
    
    # Depois que aplicamos o decorator property, podemos criar um outro método que irá alterar o valor do atributo. Novamente, essse método irá se comportar como um atributo da classe. Ou seja, ao invés de fazermos objeto.hp(10), fazemos objeto.hp = 10
    @hp.setter
    def hp(self, novo_hp):
        self._hp = novo_hp

    def atacar(self):
        print(f"{self._nome} atacou!")

    def desviar(self):
        print(f"{self._nome} desviou!")

    def evoluir(self):
        print(f"{self._nome} evoluiu!")

def mostrar(objeto: Pokemon):
    print(objeto.get_nome())

if __name__ == "__main__":
    
    # Aqui estamos instanciando a classe Pokemon. Essa classe já está sendo inicializada com os atributos nome, tipo e hp
    pikachu = Pokemon(
        nome="Pikachu",
        tipo="Elétrico",
        hp=60
    )

    # Estamos instanciando a classe Pokemon, gerando um novo objeto. Podemos criar infinitos objetos a partir de uma classe, o limite será a quantidade de memória do computador.
    charmander = Pokemon(
        nome="Charmander",
        tipo="Fogo",
        hp=120
    )

    # session.query(Pokemon).all()

    [pikachu, charmander]

    # Abaixo estamos chamando os métodos desse objeto criado a partir da classe Pokemon. O método set_tipo altera o valor do atributo _tipo do objeto. Ou seja, é a partir do atributo self que o valor é alterado.
    # Nesse caso, o tipo do pokemon está sendo alterado de Elétrico para Aquático
    print(pikachu.get_tipo())
    pikachu.set_tipo("Aquático")
    print(pikachu.get_tipo())

    print(pikachu.hp)
    pikachu.hp = 50
    print(pikachu.hp)


class Celular:
    def __init__(self) -> None:
        self._fabricante = "Samsung"


class Usuario:
    id: int
    email: str
    senha: str

class Celular:
    def __init__(self) -> None:
        self._ligado = False

    def ligar(self):
        self._ligado = True

    def desligar(self):
        self._ligado = False

    def esta_ligado(self):
        return self._ligado

samsung = Celular()
print("Celular instanciado")
print("Ligado" if samsung.esta_ligado() else "Desligado")
samsung.ligar()
print("Ligado" if samsung.esta_ligado() else "Desligado")

mostrar(pikachu)