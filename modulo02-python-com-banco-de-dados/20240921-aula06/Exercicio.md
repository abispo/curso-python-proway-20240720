# Exercício

Nesse exercício, você terá que criar as models e os seus relacionamentos, para salvar os dados que serão trazidos via API.

A partir da chamada da API de pokémons, você irá precisar salvar o seguinte:

* Na tabela `tb_pokemons`, você vai precisar salvar os dados dos seguintes campos do retorno da API:
    * id (será a chave primária da tabela)
    * base_experience
    * height
    * name
    * weight

* Na tabela `tb_habilidades`, você vai precisar salvar as informações das habilidades que são trazidas no campo '`abilities`'. Você irá salvar os dados:
    * id (Você irá pegar o id pelo campo url)
    * name
    * slot

* Na tabela `tb_pokemons_habilidades`, você vai precisar salvar o id do pokémon e o id da habilidade que ele possui, ou seja, essa tabela será uma tabela associativa entre as tabelas `tb_pokemons` e `tb_habilidades`

* Na tabela `tb_tipos`, você vai precisar salvar as informações dos tipos que são trazidas no campo '`types`'. Você irá salvar os dados:
    * id (Você irá pegar o id pelo campo url)
    * name
    * slot

* Na tabela `tb_pokemons_tipos`, você vai precisar salvar o id do pokémon e o id do tipo que ele possui, ou seja, essa tabela será uma tabela associativa entre as tabelas `tb_pokemons` e `tb_tipos`

Detalhe: Caso o registro em qualquer tabela já exista, você irá atualizar com os novos dados.