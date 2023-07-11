# Conjunto de dados - Dataset

Este dataset template é um conjunto de automatizações desenvolvidas pela Diretoria Central de Transparência Ativa - DCTA/CGE para criação, documentação, validação e publicação (criação e atualização em instâncias do CKAN) de conjunto de dados ou datasets.

Para escalarecimento sobre o fluxo completo de abertura de dados, favor consultar o [Manual do Portal de Dados Abertos de Minas Gerais](https://transparencia-mg.github.io/manual-dados-mg).

### Funcionalidades:

- Documentação de acordo com especificação de qualidade de metadados sem fricção ([fricitonless](https://specs.frictionlessdata.io/#overview)).
- Controle de versões da documentação e dos dados via Git e GitHub.
- Conversão automatizada de base de dados em Excel para formato tabular aberto (csv), caso necessário.
- Validação automatizada dos metadados e dos dados do conjunto, com demonstração de erros de validação, caso haja.
- Publicação automatizada (criação e atualização em instâncias do CKAN) do conjunto criado, documentado e validado.

### Como participar

A configuração deste dataset template está sendo feita de forma aberta e colaborativa no [GitHub](https://github.com/transparencia-mg/new-dataset-template).
Existem duas alternativas para enviar sua contribuição:

- [Issues](https://github.com/transparencia-mg/new-dataset-template/issues): Para iniciar uma discussão sobre melhorias de funcionalidades.
- [Pull requests](https://github.com/transparencia-mg/new-dataset-template/pulls): Para sugerir uma alteração concreta na ferramenta.

Todas as contribuições são bem vindas. Alguns exemplos são:

* Indicação de expressões imprecisas presentes na documentação;
* Sugestões para inclusão de descrições em campos específicos;
* Sugestões para clareza na organização das ideias;
* Correção de erros de ortografia e gramática.

### Setup do projeto

- Para realizar os passos descritos a seguir as etapas para construção da base de dados a ser aberta já devem ter sido finalizadas[^1].

- **Realize o fork do projeto** (utilizaremos um fork para conseguir atualizar as automatizações com maior facilidade no futuro):

![fork_projeto](https://imgur.com/uOZlh8a.png)

- Selecione a organização a qual o novo conjunto de dados será criado e preencha o nome do novo repositório (**o nome deverá ser o mesmo do conjunto que será criado na instância do CKAN**):

![fork_org_name](https://imgur.com/bqSjsyQ.png)

- **Cadastre Secrets para publicação em instância CKAN**:

![fork_settings](https://imgur.com/I3OFQwu.png)

![fork_secrets](https://imgur.com/aan0HNd.png)

![fork_new_secrets](https://imgur.com/Xg2TLCd.png)

- **Deverão ser criadas dois secrets**:
    - CKAN_HOST: Instância CKAN desejada, exemplo: `https://homologa.cge.mg.gov.br`
    - CKAN_KEY_USUARIO_GITHUB: se meu usuário GitHub é `gabrielbdornas` este secret será `CKAN_KEY_GABRIELBDORNAS`.
        - **Necessário criar um novo API Token na instância CKAN desejada**:

![ckan_chave](https://imgur.com/Dr1VxG8.png)

![ckan_chave_token](https://imgur.com/TpUQoLM.png)

![ckan_chave_nome](https://imgur.com/AwD8hgc.png)

![ckan_chave_criada](https://imgur.com/4qgD7HS.png)

- Cadastrar GitHub pages para mostrar relatório de validação:

![fork_settings](https://imgur.com/I3OFQwu.png)

![fork_pages](https://imgur.com/QMSmQ78.png)

![fork_pages](https://imgur.com/dHStfzi.png)

- Para rodar o processo automatiado basta incluir base de dados a ser aberta na pasta `upload` do novo repositório forkado e configurado.

[^1]: [Ciclo de Abertura, Documentação, Validação e Publicação](https://transparencia-mg.github.io/manual-dados-mg/0.1/2.%20Ciclo%20de%20publica%C3%A7%C3%A3o%20de%20dados/006_etapas_abertura/).
