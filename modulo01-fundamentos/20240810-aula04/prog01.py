"""
Entrada e saída (I/O) de arquivos em Python

Leitura de arquivos .txt

"""

import os

if __name__ == "__main__":

    if not os.path.exists("dfdsjfhsdjf"):
        print("Esse arquivo não existe")
    
    # Utilizamos a função built-in open() para abrir um arquivo.
    arquivo = open(
        file="linguagens.txt",
        mode="r"
    )

    """
    O comando acima abre o arquivo 'linguagens.txt' no modo somente-leitura. Nesse caso, não conseguimos editar o arquivo.

    No python existem 4 modos de abertura de arquivo:
        r -> Somente Leitura (read)
        w -> Somente Escrita (write)
        x -> Somente criação do arquivo (create)
        a -> Somente escrita (append)

    Enquanto o modo de abertura 'a' começa a escrever no final do arquivo, o modo de abertura w apaga o conteúdo do arquivo e escreve por cima.

    Além dos modos de abertura, podemos indicar o tipo de arquivo. Por exemplo: o modo 'rt' abre um arquivo de texto plano apenas para leitura, enquanto o modo 'wb' abre um arquivo binário para escrita. Se não for indicado, por padrão o Python considera que está sendo aberto um arquivo de texto plano.

    Também podemos utilizar o '+' para abrir o arquivo no modo leitura e escrita (r+)
    
    """

    # O método read() lê o conteúdo do arquivo e retorna como string
    print(arquivo.read())

    # Sempre quando terminarmos de manipular o arquivo, é muito importante fecharmos ele. Utilizamos o método close() para isso
    arquivo.close()
    
    print('*'*50)

    with open("linguagens.txt", "r", encoding="utf-8") as arquivo:

        # Lendo os 5 primeiros bytes(caracteres do arquivo)
        print(arquivo.read(5))

        # O método readline() lê o conteúdo da linha. Como já lemos os primeiros 5 caractes do arquivo, ele vai retornar os caracteres restantes da linha
        print(arquivo.readline())

        # Podemos indicar também a quantidade de caracteres que queremos ler na linha
        print(arquivo.readline(1))

        # O método tell() indica a posição atual do cursor no arquivo
        print(arquivo.tell())
        
        # O método readlines lê o arquivo e retorna uma lista de strings, com cada string representando uma linha. Podemos indicar a quantidade de caracteres que queremos ler, porém sempre a linha inteira será retornada
        print(arquivo.readlines(5))
    
        print(arquivo.readlines())

        print(arquivo.readlines())
        # Como o cursor chegou ao final do arquivo, nenhum conteúdo será exibido. Precisamos "rebobinar" o cursor para conseguir ler o conteúdo do arquivo novamente. Utilizamos para isso o método seek
        arquivo.seek(0)
        print(arquivo.readlines())
