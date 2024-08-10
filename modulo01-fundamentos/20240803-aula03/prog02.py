"""
Funções (Procedures)

Parâmetros arbitrários

No Python, podemos criar funções que recebem uma quantidade arbitrária (qualquer) de parâmetros. É um recurso bastante utilizado quando criamos decorators.
"""

def calcula_media_sensor(*args):
    return sum(args) / len(args)

def mostra_info_usuario(**kwargs):
    return kwargs

if __name__ == "__main__":
    
    print(calcula_media_sensor(0.6, 0.4, 1.1, 1.2, 1.5))
    print(calcula_media_sensor(0.6, 1.1))

    usuario1 = {
        "nome": "João",
        "idade": 34
    }

    usuario2 = {
        "nome": "Maria",
        "idade": 30,
        "genero": "Feminino",
        "cidade": "Blumenau"
    }

    mostra_info_usuario(nome="Carlos", cidade="Brusque")
    mostra_info_usuario(nome="Celso", cidade="Blumenau", idade=18)
    mostra_info_usuario(**usuario1)
    mostra_info_usuario(**usuario2)