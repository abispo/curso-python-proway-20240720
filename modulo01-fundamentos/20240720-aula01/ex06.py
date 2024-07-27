# Crie um programa que leia três notas (nota1, nota2 e nota3) de um aluno e calcule a média. Se a média for menor do que 5, imprima a mensagem "Reprovado". Se a média for maior ou igual a 5 e menor do que 7, imprima "em recuperação". Se a média for maior ou igual a 7, imprima "Aprovado".

if __name__ == "__main__":

    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media < 5:
        print(f"Sua média é de {media:.2f}. Você está reprovado.")

    elif media >= 5 and media < 7:
        print(f"Sua média é de {media:.2f}. Você está em recuperação.")

    else:
        print(f"Sua média é de {media:.2f}. Você está aprovado.")