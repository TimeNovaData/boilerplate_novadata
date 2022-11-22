# Projeto de modelo
## Intuito e modo de usar
Esse é um projeto de modelo, criado para facilitar a configuração inicial dos nossos sitemas.

## Features
Esse modelo conta com as seguintes features:
- Toda a configuração necessária para subir um projeto no Heroku.
- App home com sidebar padrão dos nossos projetos.
- App front_assets com diretórios padrão usuados pelos nossos fronts.
- Design system.
- SVG viewer.
- Barra de notificações (apenas no front).
- Configuração do Django Admin Docs.

## Get started

1 - Crie uma venv e ative-a com os seguintes comandos:

Linux
```shell
virtualenv -p python .venv_nome_projeto
source .venv_nome_projeto/bin/activate
```

Windows
```shell
python -m venv .venv_nome_projeto
.\.venv_nome_projeto\Scripts\activate
```

2 - Instale o Django
```shell
pip install django
```

3 - Crie um projeto Django utilizando o comando abaixo
(lembre-se de trocar o fim do comando pelo nome do seu projeto)
```shell
django-admin startproject --template https://github.com/TimeNovaData/heroku_modelo/raw/master/project_name.zip --name=Procfile --name=package.json --name=README.md nome_do_projeto
```

4 - Instale as dependências Python
```shell
pip install -r requirements.txt
```

5 - Instale as dependências Node
```shell
npm install
```

6 - Crie um banco de dados
```shell
python manage.py migrate
```

7 - Crie um super usuário
```shell
python manage.py createsuperuser
```

8 - Rode o projeto
```shell
python manage.py runserver
```

Depois disso você pode criar o repositório Git, a app no Heroku, conecar ambas e fazer o deploy!

## Deseja fazer modificações?
Basta baixar o projeto em sua máquina, modificar o que desejar, apagar e recriar o arquivo .zip e fazer o pull request como de costume!

Obrigado por contribuir! o/
