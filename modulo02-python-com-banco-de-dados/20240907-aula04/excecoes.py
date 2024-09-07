
class ValorDeSaqueInvalido(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Você está tentando sacar R$ {}, porém só possui R$ {} na conta".format(
            *args
        ))

class ValorDeDepositoInvalido(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("Você deve sacar um valor maior do que zero. Você informou R$ {}".format(
            *args
        ))
