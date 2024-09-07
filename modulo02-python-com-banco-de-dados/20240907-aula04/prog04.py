"""
Programação Orientada a Objetos em Python

Composição
Composição ocorre quando uma classe compõe ou é composta por outras classes

"""

from random import shuffle

class Carta:
    def __init__(self, numero: str, naipe: str) -> None:
        self._numero = numero
        self._naipe = naipe

    # __str__ é um método mágico do python que é chamado quando o objeto é lido na tela. No caso abaixo, estamos indicando que quando ele for lido, será retornada uma string formada pelo numero e pelo naipe
    def __str__(self) -> str:
        return "{}{}".format(
            self._numero,
            self._naipe
        )

    # __repr__ é outro método mágico utilizado quando um objeto dentro de um container é impresso. Abaixo também estamos alterando o seu comportamento
    def __repr__(self) -> str:
        return "{}{}".format(
            self._numero,
            self._naipe
        )


class Baralho:
    def __init__(self) -> None:
        self._cartas = []
        self._numeros = [
            '2', '3', '4', '5',
            '6', '7', '8', '9', '10',
            'J', 'Q', 'K', 'A'
        ]

        self._naipes = [
            "\u2660", "\u2665", "\u2666", "\u2663"
        ]


        for numero in self._numeros:
            for naipe in self._naipes:
                self._cartas.append(Carta(numero=numero, naipe=naipe))

        shuffle(self._cartas)

    def __str__(self) -> str:
        return ", ".join(str(carta) for carta in self._cartas)

if __name__ == "__main__":
    baralho = Baralho()
    print(baralho)

    # Desafio: Fazer o objeto da classe Baralho ser iterável.
    # Dica: Procure os métodos mágicos __iter__ e __next__
    # Dica2: Pode utilizar o chat gpt. Mas assegure-se de que entende o que está acontecendo
