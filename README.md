# Projeto de modelo para o Heroku
## Intuito e modo de usar
Esse é um projeto de modelo, criado para facilitar a configuração para o Heroku que sempre fazemos.

Para criar um projeto com toda a configuração necessária para o Heroku basta rodar o seguinte comando:

```shell
django-admin startproject --template https://github.com/TimeNovaData/heroku_modelo/raw/master/project_name.zip --name=Procfile --name=README.md nome_do_projeto
```

Depois disso você pode criar o repositório Git, a app no Heroku, conecar ambas e fazer o deploy!

## Deseja fazer modificações?
Basta baixar o projeto em sua máquina, modificar o que desejar, apagar e recriar o arquivo .zip e fazer o pull request como de costume!

Obrigado por contribuir! o/