# Django

## Criar uma nova aplicação Django

`django-admin startproject [nome_do_projeto]`

Caso você coloque o ponto (`.`) no final do comando, o django irá criar a estrutura do projeto na pasta atual

* Criar um novo app para o projeto

`python manage.py startapp [nome_do_app]`

* Aplicar migrations já existentes que não foram aplicadas

`python manage.py migrate`

* Criar novas migrations

`python manage.py makemigrations [nome_do_app]`

* Criar um superadmin no projeto

`python manage.py createsuperuser`