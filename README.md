# Boilerplate
Um boilerplate é um projeto de modelo, criado para facilitar a configuração inicial dos nossos sitemas, trazendo algumas coisas já pré-configuradas,
assim nós só precisamos nos preocupar em desenvolver de fato o sistema.


Esse modelo conta com as seguintes features:
- Configuração do Heroku.
- Configuração do Django Admin Docs.
- Configuração do Django Rest Framework.
- Configuração do Django Spectacular.
- Configuração do Django Browser Reload.
- Configuração do Django Debug Toolbar.
- App home com sidebar padrão dos nossos projetos.
- App front_assets com diretórios padrão usuados pelos nossos fronts.
- Design system.
- SVG viewer.
- Barra de notificações (apenas no front).
- BaseViewNovadata, contanto com implementação de breadcrumbs por padrão.
- BaseNovadataAdmin, contanto com import export das models por padrão.
- Funções para construção de breadcrumbs.
- Autenticação de login por user e e-mail simultaneamente.

## Get started

- Crie uma venv e ative-a com os seguintes comandos:

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

- Instale o Django
```shell
pip install django
```

- Crie um projeto Django utilizando o comando abaixo
(lembre-se de trocar o fim do comando pelo nome do seu projeto)
```shell
django-admin startproject --template https://github.com/TimeNovaData/boilerplate_novadata/raw/master/project_name.zip --name=Procfile --name=package.json --name=README.md nome_do_projeto
```

- Entre na pasta do projeto
```shell
cd nome_do_projeto
```

- Instale as dependências Node (você pode deixar esse comando rodando e dar continuidade nos demais em outro terminal)
```shell
npm install
```

- Instale as dependências Python
```shell
pip install -r requirements-dev.txt
```

- Crie as migrations extras, um banco de dados e colete os arquivos estáticos
```shell
python manage.py makemigrations
python manage.py migrate
```

- Crie um super usuário
```shell
python manage.py createsuperuser
```

- Rode o projeto
```shell
python manage.py runserver
```

Feito! Seu projeto está rodando com diversas coisas úteis já configuradas.
Agora é só codar!!

## Deseja fazer modificações?
Basta baixar o projeto em sua máquina, modificar o que desejar, apagar e recriar o arquivo .zip e fazer o pull request como de costume!

Obrigado por contribuir! o/
