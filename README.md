# README.md

Esse é apenas uma POC para criar os templates de um HELM Chart utilizando Python e dessa forma atualizar todos os templates do ambiente de forma automatizada

Passo 01 - Clonar o repositório

Passo 02 - Gerar o arquivo de deployment do template

```
cd helm-templates-generate
python3 script.py
```

Passo 03 - Copiar o arquivo de template do deployment em `helm-templates-generate/output-templates/deployment.yaml` para `validate-template-generate/templates`

```
cd ../ 
cp -a helm-templates-generate/output-templates/deployment.yaml validate-template-generate/templates
```

Passo 04 - Validar a sintaxe do helm

```
helm template my-validate validate-template-generate/ --debug
```