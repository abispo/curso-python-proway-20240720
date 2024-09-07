"""
Programação Orientada a Objetos em Python

Polimorfismo
Polimorfismo siginifica "muitas formas", ou seja, uma função ou método pode ser chamado de várias maneiras, trazendo diferentes comportamentos
"""

class Funcionario:
    
    def __init__(self, nome: str) -> None:
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome

    def calcular(self):
        raise NotImplementedError


class FuncionarioCLT(Funcionario):

    def __init__(self, nome: str, salario: float) -> None:
        self._salario = salario
        super().__init__(nome)

    def calcular(self) -> float:
        return self._salario


class FuncionarioTerceirizado(Funcionario):
    def __init__(self, nome: str, quantidade_horas_trabalho: int, valor_hora_trabalho: float) -> None:
        self._quantidade_horas_trabalho = quantidade_horas_trabalho
        self._valor_hora_trabalho = valor_hora_trabalho
        super().__init__(nome)

    def calcular(self) -> float:
        return self._quantidade_horas_trabalho * self._valor_hora_trabalho


class FuncionarioComissionado(Funcionario):
    def __init__(self, nome: str, valor_total_vendido: float, comissao: float) -> None:
        self._valor_total_vendido = valor_total_vendido
        self._comissao = comissao
        super().__init__(nome)

    def calcular(self) -> float:
        return self._valor_total_vendido * (self._comissao / 100)