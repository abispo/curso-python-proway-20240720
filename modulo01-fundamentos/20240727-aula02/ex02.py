# 2. Escreva um programa que receba números pelo terminal. Se o usuário digitar o número 0, o programa para de receber números pelo terminal e retorna uma lista dos quadrados desses números.

if __name__ == "__main__":
    

    lista_numeros = []

    while True:
        
        numero = int(input("Informe um número: "))

        if numero == 0:
            print("Informado número 0.")
            break

        lista_numeros.append(numero)

    # Utilizando list-comprehension
    lista_quadrados = [numero * numero for numero in lista_numeros]

    print(f"Lista dos quadrados: {lista_quadrados}")