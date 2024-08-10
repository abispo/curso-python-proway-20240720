"""
Funções (Procedures)

Funções recursivas

Uma função recursiva é uma função que chama a si mesma. Um exemplo clássico é a função fatorial.

!5 = 5 * 4 * 3 * 2 * 1 = 120

"""

def fatorial_nao_recursivo(numero):
    contador = numero
    total = numero

    while contador > 1:
        total = total * (contador - 1)
        contador -= 1   # contador = contador - 1

    return total

def fatorial_recursivo(numero):
    if numero == 1:
        return numero
    
    return numero * fatorial_recursivo(numero - 1)

if __name__ == "__main__":
    print(fatorial_nao_recursivo(5))
    print(fatorial_recursivo(5))