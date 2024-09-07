"""
Programação Orientada a Objetos em Python

Herança
Herança acontece quando um classe (classe filha ou subclasse) herda atributos e métodos de uma outra classe (classe pai/mãe ou superclasse)
"""

from contas import ContaCorrente, ContaInvestimento
from excecoes import ValorDeDepositoInvalido

if __name__ == "__main__":

    conta_viacredi = ContaCorrente(
        nome="Conta Corrente ViaCredi", saldo=100
    )

    conta_viacredi.depositar(150.50)
    conta_viacredi.sacar(85)
    print(conta_viacredi.saldo)

    conta_investimento_caixa = ContaInvestimento(
        "CDB Caixa", 1.5, 100
    )
    conta_investimento_caixa.render()
    print(conta_investimento_caixa.saldo)

    try:
        conta_investimento_caixa.sacar(1000)
        
    except Exception as exc_info:
        print(exc_info)

    try:
        conta_investimento_caixa.depositar(-500)

    except ValorDeDepositoInvalido as exc_info:
        print(exc_info)