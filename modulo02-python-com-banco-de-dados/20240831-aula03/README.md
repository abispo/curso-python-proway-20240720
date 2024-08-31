# Desafio: Trabalhando com Classes, Objetos, Atributos e Métodos.

Iremos implementar algumas funcionalidades da batalha de RPG, que nós fizemos para aprender como funciona o laço `while` na segunda aula do módulo de fundamentos [Link para o arquivo](https://github.com/abispo/curso-python-proway-20240720/blob/main/modulo01-fundamentos/20240727-aula02/prog03.py). Você irá implementar, utilizando orientação a objetos, as seguintes funcionalidades (Lembre-se de criar os métodos get e set para os atributos privados que precisarão ser acessados):

1. classe `Heroi`, que terá as seguintes características:
    * Atributos:
        * _nome
        * _ataque
        * _defesa
        * _vitalidade

    * Métodos:
        * atacar
        * defender
        * perder_vida(quantidade)

2. classe `Monstro`, que terá exatamente os mesmos atributos e os mesmos métodos que a classe `Heroi`.

3. classe `Rodada`. Essa classe irá representar uma rodada da batalha. Em cada rodada, o herói ataca primeiro, e o monstro defende. Após isso, o herói defende e o monstro ataca. Com isso finalizamos a rodada. Essa classe terá as seguintes características:
    * atributos
        * _heroi
        * _monstro

    * métodos
        * iniciar

4. Crie a classe `Batalha`, que irá representar a batalha em si. Essa batalha deverá ocorrer enquanto nenhum dos personagens morrer. Você definirá quais os atributos e os métodos dessa classe que melhor se funcionarão para replicarmos o comportamento do código da aula anterior.