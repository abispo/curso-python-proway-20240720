from excecoes import ValorDeDepositoInvalido, ValorDeSaqueInvalido


class ContaFinanceira:

    def __init__(self, nome: str, saldo: float=0) -> None:
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
        if valor > self._saldo:
            raise ValorDeSaqueInvalido(valor, self._saldo)
        self._saldo = self._saldo - valor
        return valor

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValorDeDepositoInvalido(valor)
        self._saldo = self._saldo + valor


class ContaCorrente(ContaFinanceira):
    pass


class ContaInvestimento(ContaFinanceira):
    def __init__(self, nome: str, taxa: float, saldo: float = 0) -> None:
        self._taxa = taxa
        super().__init__(nome, saldo)

    def render(self):
        self._saldo = self._saldo + (self._saldo * (self._taxa / 100))