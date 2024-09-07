"""
Programação Orientada a Objetos em Python

Encapsulamento
É o processo onde "protegemos" dados internos do objeto, e definimos as "interfaces" públicas que darão acesso aos atributos e/ou métodos privados do objeto, sendo possível assim alterar o seu estado.

"""

class ContaBancaria:
    
    def __init__(self, nome: str, saldo: float = 0) -> None:
        self._nome = nome
        self._saldo = saldo

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome) -> None:
        self._nome = novo_nome

    @property
    def saldo(self) -> float:
        return self._saldo
    
    # Nesse método, indicamos que o parâmetro 'valor' deve ser do tipo float. Também indicamos que o valor de retorno do método será 'None' (pois nesse caso não utilizamos a palavra reservada return)
    def depositar(self, valor: float) -> None:
        self._saldo = self._saldo + valor

    # Nesse método, indicamos que o parâmetro 'valor' deve ser do tipo float. Também indicamos que o valor de retorno do método será do tipo 'float', pois estamos retornando o valor que foi sacado.
    # Porém, sabemos que o Python não força os valores passados aos parâmetros serem do tipo que foi especificado.
    def sacar(self, valor: float) -> float:
        self._saldo = self._saldo - valor
        return valor
    
if __name__ == "__main__":

    texto = """
ESCOLHA UMA OPÇÃO:
0 - SAIR
1 - VER SALDO
2 - DEPOSITAR
3 - SACAR
"""

    conta_bancaria_viacredi = ContaBancaria(nome="Conta Corrente ViaCredi")

    while True:
        print(texto)
        opcao = int(input("Informe a opção: "))