# Tipos de dados em Python
# Strings

# Strings são cadeias de caracteres, que podem conter qualquer tipo de caractere (letras, numeros, simbolos, etc)

# Podemos representar string no python utilizando aspas duplas ou aspas simples.


if __name__ == "__main__":
    # O comando input recebe um valor via terminar. Importante lembrar que qualquer coisa digitada pelo terminal, é considerada uma string
    nome = input("Informe o seu nome: ")

    # Maneiras antigas de concatenar strings
    print("Olá " + nome + ", Bem vindo(a) ao curso de Python")
    print("Olá %s, Bem-vindo(a) ao curso de Python" % nome)

    # Maneiras modernas de concatenar strings
    print("Olá {}, Bem-vindo(a) ao curso de Python".format(nome))
    print(f"Olá {nome}, Bem-vindo(a) ao curso de Python")

    setor = input("Informe o seu setor: ")
    funcao = input("Informe a sua função: ")

    saida = """
NOME: {}
SETOR: {}
FUNÇÃO: {}
""".format(nome, setor, funcao)
    
    print(saida)