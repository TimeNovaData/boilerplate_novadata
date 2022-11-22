# Boilerplate
Um boilerplate é um projeto de modelo, criado para facilitar a configuração inicial dos nossos sitemas, trazendo algumas coisas já pré-configuradas,
assim nós só precisamos nos preocupar em desenvolver de fato o sistema.


Esse modelo conta com as seguintes features:
- Toda a configuração necessária para subir um projeto no Heroku.
- App home com sidebar padrão dos nossos projetos.
- App front_assets com diretórios padrão usuados pelos nossos fronts.
- Design system.
- SVG viewer.
- Barra de notificações (apenas no front).
- Configuração do Django Admin Docs.

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

- Instale as dependências Python
```shell
pip install -r requirements.txt
```

- Instale as dependências Node (você pode deixar esse comando rodando e dar continuidade nos demais em outro terminal)
```shell
npm install
```

- Crie um banco de dados
```shell
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

Depois disso você pode criar o repositório Git, a app no Heroku, conecar ambas e fazer o deploy!

## Deseja fazer modificações?
Basta baixar o projeto em sua máquina, modificar o que desejar, apagar e recriar o arquivo .zip e fazer o pull request como de costume!

Obrigado por contribuir! o/
