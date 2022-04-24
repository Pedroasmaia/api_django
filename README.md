# Projeto Library
## Sumarry:

- Language: <i>Python</i>
- Framework: <i>Django</i>

## Steps:
1. Configurações iniciais
    - Criar pasta do projeto:
        ~~~ 
        mkdir library
        cd .\library
    - Virtualizar máquina Python:
        ~~~
        python 3.7 -m venv venv
    - Ativar VM
        ~~~
        library\venv\Scripts\activate
    - Iniciar Projeto
        ~~~
        django-admin startproject library . 

2. Instalando Apps
    - Cadastro de livros:
        ~~~
        django-admin startapp books
    - Rode o servidor com: 
        ~~~
        python manage.py runserver
    - Criar as tabelas dentro do banco de dados:
        ~~~
        python manage.py migrate
    - Dentro de settings.py do Projeto Library, colocamos em *INSTALLED_APPS*, o *rest_framework* e o app *books* que vamos utilizar