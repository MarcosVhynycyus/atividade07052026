# Rede de Cinemas

Este projeto atende ao estudo de caso de uma rede de cinemas, propondo um sistema simples para organizar cinemas, filmes, sessoes, registros de publico, usuarios e totalizacoes. A solucao foi mantida enxuta, coerente com a proposta da atividade e focada em demonstrar a ligacao entre requisitos, diagramas UML, arquitetura em camadas e implementacao.

## Parecer sobre a solucao

O projeto apresenta uma estrutura adequada para fins didaticos. A documentacao identifica os principais requisitos funcionais, regras de negocio e fluxos essenciais do dominio. A implementacao segue a separacao MVC + Service + Repository, deixando a interface de terminal nas views/pages, a entrada das requisicoes nos controllers, as validacoes nos services e o acesso ao SQLite nos repositories.

O caso de uso implementado de forma completa e o registro de publico de uma sessao. A evolucao adiciona autenticacao, autorizacao por perfil e manutencao administrativa de cinemas, filmes, sessoes e registros de publico.

## Entidades principais do dominio

- Cinema: unidade fisica da rede, com cidade, estado, endereco e capacidade.
- Filme: obra exibida nas sessoes, com genero, diretor, elenco, duracao e classificacao.
- Sessao: exibicao de um filme em um cinema, sala e horario especificos.
- RegistroPublico: quantidade de espectadores registrada para uma sessao.
- Usuario: acesso autenticado com perfil `admin` ou `staff`.
- Genero, Diretor e Ator: conceitos usados para descrever e consultar os filmes.

## Documentacao

A pasta `docs` contem os documentos e diagramas da atividade:

- `requisitos.md`: requisitos funcionais, nao funcionais e regras de negocio.
- `arquitetura.md`: organizacao da solucao e camadas da aplicacao.
- `casos_de_uso.puml`: visao geral dos atores e casos de uso.
- `classes_dominio.puml`: diagrama principal das classes de dominio.
- `classes_dominio_registro_publico.puml`: recorte do dominio para o caso de uso implementado.
- `classes_dominio_filmes.puml`: recorte do dominio para filmes, genero, diretores e elenco.
- `atividade_registrar_publico.puml`: fluxo de atividade do registro de publico.
- `atividade_consultar_totalizacoes.puml`: fluxo de atividade das totalizacoes.
- `sequencia_registrar_publico.puml`: interacao entre View, Controller, Service, Repository e SQLite.
- `sequencia_consultar_totalizacoes.puml`: sequencia da consulta de totalizacoes.
- `atividade_autenticacao_autorizacao.puml`: fluxo de login e decisao de perfil.
- `atividade_manter_cadastros_admin.puml`: fluxo generico de manutencao administrativa.
- `sequencia_manter_cadastro_admin.puml`: sequencia generica de uma operacao administrativa.

## Implementacao

A pasta `src` concentra a aplicacao em terminal:

- `src/config`: conexao e banco SQLite.
- `src/pages`: login, menu de staff e menu administrativo.
- `src/modules`: modulos de cinema, filme, sessao, publico, relatorio e usuario.
- `src/app.py`: montagem das dependencias e configuracao inicial.
- `src/main.py`: ponto de entrada da aplicacao.

O arquivo `init.py`, na raiz, cria as tabelas e insere dados iniciais para teste.

## Como executar

```bash
python3 src/main.py
```

O banco sera criado em `src/config/database.db`.

Usuarios iniciais:

- Admin: `admin` / `admin123`.
- Staff: `staff` / `staff123`.
