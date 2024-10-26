# Desafios em Django

## 1. Criar uma página de estatísticas no site

Na página principal do pacote `enquetes`, haverá um link para a página principal do pacote `estatisticas`, onde mostraremos as seguintes estatísticas sobre as perguntas e opções:
* Quantas perguntas estão cadastradas
* Quantas opções estão cadastradas
* Média de opções por pergunta
* Uma lista com as 5 primeiras perguntas ordenadas pela quantidade de votos que recebeu (mais para menos)

Dica: Para a última estatística, você pode utilizar o método `annotate` para agregar as informações da consulta. A documentação está no link a seguinte: https://docs.djangoproject.com/en/5.1/topics/db/aggregation/.

Ou seja, o passo a passo será:
* Criar o app estatisticas
* Registrar o app na lista `INSTALLED_APPS` no arquivo `settings.py`
* Criar uma rota index nesse pacote estatisticas
* Essa rota index exibirá as estatísticas

## 2. Na página de resultados, criar um estrutura de feedback de perguntas

Quando o usuário vota, ele é redirecionado a página de resultados. Nessa página será exibida uma estrutura onde o usuário pode dar uma nota de 1 a 5 para a pergunta. Se quiser o usuário poderá dar uma nota a essa pergunta, e essa nota será armazenada em uma tabela de notas de perguntas. Quando o usuário escolher a nota e clicar no botão enviar, essa nota será salva na tabela e o usuário será redirecionado para a página principal.

Sinta-se livre para utilizar o elemento que quiser para exibir as notas, como o elemento `select` ou o `input type radio`. Altere a página de estatísticas, adicionando a média da pergunta a listagem das perguntas com mais votos. Exemplo:

```
Quem descobriu o Brasil? (6 votos) (média 4.7)
Que ano o Brasil foi descoberto? (4 votos) (média 4.8)
Em que ano houve a Proclamação da República? (1 voto) (média 4.1)
```