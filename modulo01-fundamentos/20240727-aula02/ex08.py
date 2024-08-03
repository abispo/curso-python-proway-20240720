"""
8. Escreva um programa em Python que inverta uma lista de números. Exemplo:

lista = [4, 7, 8, 1, 9]
lista_invertida = [9, 1, 8, 7, 4]
"""

if __name__ == "__main__":

    lista = [4, 7, 8, 1, 9]
    lista_invertida = []

    # Primeiro método
    for numero in lista:
        lista_invertida.insert(0, numero)

    print(lista_invertida)

    # Segundo método (fazendo o slicing (fatiamento) de lista)
    print(lista[::-1])

    # Podemos passar até 3 argumentos pro slice:
    # O primeiro é o indice de inicio (inclusivo)
    # O segundo é o indice final (exclusivo)
    # O terceiro é o step (de quantos em quantos itens serão pegos)

    # O slice pode ser usado na cópia de listas, pois sempre será gerada uma lista nova.

    # copia_da_lista = lista_invertida
    copia_da_lista = lista_invertida
    print(copia_da_lista)

    copia_da_lista.append(10)
    print(copia_da_lista)
    print(lista_invertida)
    lista_invertida.clear()
    print(copia_da_lista)
    print(lista_invertida)

    # Quando quisermos fazer uma copia de listas, precisamos utilizar o método .copy ou fazer o slice da lista
