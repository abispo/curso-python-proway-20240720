# 1. Escreva um programa que receba um número maior do que 1 pelo terminal. Em seguida, o programa retorna a soma de 1 até esse número.

if __name__ == "__main__":
    
    numero = int(input("Informe um número: "))

    if numero < 1:
        print("O número deve ser maior ou igual a 1.")

    else:
        # Primeira maneira
        contador = 1
        soma = 0

        while contador <= numero:
            soma = soma + contador
            # soma += contador  # Mesma coisa da linha anterior

            contador += 1
        
        print(f"A soma de 1 até {numero} é igual a {soma}.")

        # Segunda maneira (usando a função range())
        soma = 0

        for contador in range(1, numero + 1):
            soma += contador

        print(f"A soma de 1 até {numero} é igual a {soma}.")