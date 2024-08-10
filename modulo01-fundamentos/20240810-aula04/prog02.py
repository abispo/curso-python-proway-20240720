"""
Entrada e saída (I/O) de arquivos em Python

Escrita de arquivos .txt

"""

if __name__ == "__main__":

    print("== LISTA DE COMPRAS ==")

    # O modo de abertura 'w' cria um novo arquivo se não existir, e se existir, sobrescreve o seu conteúdo
    with open("lista_de_compras.txt", "w", encoding="utf-8") as arquivo:
        
        for _ in range(3):
            item = input("Informe um item de compra: ")

            # O método write() escreve um texto no arquivo. Abaixo utilizamos o caractere especial '\n' para criar uma nova linha
            arquivo.write(f"{item}\n")

    itens_obrigatorios = ["Damasco\n", "Uva\n"]

    # O modo de abertura 'a' cria o arquivo se não existir, e se existir, começa a escrever a partir do final do arquivo.
    with open("lista_de_compras.txt", "a", encoding="utf-8") as arquivo:

        # O método writelines() recebe uma lista de strings e escreve no arquivo
        arquivo.writelines(itens_obrigatorios)

