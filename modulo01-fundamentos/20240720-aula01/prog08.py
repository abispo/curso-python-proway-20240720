# Laço de condição if... elif... else

if __name__ == "__main__":
    
    valor = float(input("Informe o valor total do pedido: "))

    if valor <= 500:
        desconto = 5

    elif valor >= 500.01 and valor <= 2500:
        desconto = 10

    elif valor >= 2500.01 and valor <= 5000:
        desconto = 15

    else:
        desconto = 20

    print("O valor total do pedido foi de R$ {}. Você ganhou {}% de desconto.".format(
        valor, desconto
    ))