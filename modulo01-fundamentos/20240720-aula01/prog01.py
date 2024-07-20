# Isso é um comentário

"""
No Python, não existe um caractere específico para comentários multi linha. Para isso, utilizamos a string multilinha.

"""

# A primeira linha, é uma expressão em Python
# Uma expressão consiste de um conjunto de operadores e operandos, que geram um valor.

# Como boa prática, sempre iniciamos o script principal da nossa aplicação com a expressão "if __name__ == '__main__'". Isso indica que estamos executando o módulo principal do nosso programa, o qual chamará os outros módulos

# Sempre que tivermos um comando if, else, while, etc, precisamos terminar a linha com 2 pontos (:), o que indica que estamos criando um novo bloco de código. Sempre que criarmos um novo bloco de código, precisamos identar a primeira linha desse bloco. Por padrão, o VSCode já cria uma identação de 4 espaços.

# Uma vez definida a identação dentro do bloco, não podemos ter linhas dentro desse bloco com identações diferentes.
if __name__ == "__main__":
    print("Olá mundo", end=''); print("Tchau")
