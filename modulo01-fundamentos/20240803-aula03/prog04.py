"""
Funções (Procedures)

Funções lambda

Existe a possibilidade de criarmos funções anônimas (função sem nome definido) dentro do Python. Chamamos essas funções de funções lambda.

Procedural
Orientado a Objetos
Funcional

"""

def nota_maior(lista_usuarios):
    lista_notas = []
    for usuario in lista_usuarios:
        if usuario.get("nota_final") >= 7:
            lista_notas.append(usuario)

    return lista_notas

def verificar(usuario):
    return usuario.get("nota_final") >= 7

if __name__ == "__main__":

    # Exemplo de função lambda que apenas retorna um valor
    x = lambda: "ola"
    y = lambda p: p

    print(x())
    print(y(10))

    lista_usuarios = [
        {"nome": "Maria", "nota_final": 8},
        {"nome": "João", "nota_final": 6.5},
        {"nome": "Viviane", "nota_final": 10},
        {"nome": "Eduardo", "nota_final": 5},
        {"nome": "Gustavo", "nota_final": 3},
    ]

    # Exemplo chamando uma função de maneira tradicional
    print(nota_maior(lista_usuarios))

    # Exemplo chamando uma função criada especificamente para o filter
    print(list(filter(verificar, lista_usuarios)))

    # Exemplo utilizando uma função anônima (lambda)
    print(list(filter(lambda x: x.get("nota_final") >= 7, lista_usuarios)))

    print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))

    # A função filter retorna uma lista de valores, caso a função aplicada nos itens da sequencia retorne True

    # A função map retorna uma lista de valores, aplicando a função passada como parâmetro em cada item da lista