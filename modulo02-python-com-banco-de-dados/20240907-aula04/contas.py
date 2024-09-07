
class ContaFinanceira:

    def __init__(self, nome: float, saldo: float=0) -> None:
        self._nome = nome
        self._saldo = saldo

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome

    @property
    def saldo(self) -> float:
        return self._saldo
    
    def sacar(self, valor: float) -> float:
        pass

    def depositar(self, valor: float) -> None:
        pass