# 4. Escreva um programa que converta uma lista de inteiros em apenas 1 inteiro

if __name__ == "__main__":
    lista = [4, 7, 10, 24]

    saida = ""

    for numero in lista:
        saida = f"{saida}{numero}"

    print(f"Saída: {saida}")

    # Maneira alternativa
    print("".join(str(numero) for numero in lista))