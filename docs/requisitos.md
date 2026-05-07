# Rede de Cinemas - Requisitos e Regras de Negocio

## Escopo

Sistema enxuto para centralizar filmes, cinemas, sessoes e registros de publico de uma rede de cinemas. A implementacao prioriza o caso de uso completo "Registrar publico de uma sessao", mantendo consultas de apoio para sessoes, filmes, cinemas e totalizacoes.

## Atores

- Funcionario/Administrador: mantem a operacao da rede, organiza sessoes e registra publico.
- Espectador: consulta filmes, sessoes e informacoes basicas de exibicao.

## Requisitos funcionais

- RF01 - Listar cinemas cadastrados, com cidade, estado, endereco e capacidade.
- RF02 - Listar filmes em cartaz, com genero, diretor, elenco, classificacao e duracao.
- RF03 - Listar sessoes por cinema, filme, sala, horario e ocupacao atual.
- RF04 - Registrar o publico de uma sessao.
- RF05 - Totalizar publico por sessao, por filme e por cinema.
- RF06 - Consultar informacoes de filmes, incluindo genero, diretor e elenco.

## Requisitos nao funcionais

- RNF01 - A aplicacao deve persistir dados em SQLite.
- RNF02 - A arquitetura deve separar View, Controller, Service e Repository.
- RNF03 - A interface deve ser simples e executada em terminal.
- RNF04 - O sistema deve permitir evolucao de entidades sem alterar todas as camadas.
- RNF05 - As regras de negocio devem ficar concentradas nos services.

## Regras de negocio

- RN01 - Uma sessao pertence a um cinema e exibe um unico filme.
- RN02 - Um cinema pode possuir varias sessoes.
- RN03 - Um filme pode estar em varias sessoes e em diferentes cinemas.
- RN04 - O publico registrado em uma sessao nao pode ultrapassar a capacidade do cinema.
- RN05 - O registro de publico deve ter quantidade inteira positiva.
- RN06 - A totalizacao de publico por filme soma todos os registros das sessoes daquele filme.
- RN07 - A totalizacao de publico por cinema soma todos os registros das sessoes daquele cinema.
- RN08 - A organizacao das sessoes deve considerar a duracao do filme e o intervalo minimo cadastrado entre exibicoes.

## Caso de uso implementado

Registrar publico de uma sessao:

1. O funcionario consulta as sessoes em cartaz.
2. O funcionario informa o identificador da sessao.
3. O funcionario informa a quantidade de espectadores da sessao.
4. O sistema valida se a sessao existe.
5. O sistema valida se a quantidade e positiva.
6. O sistema valida se a nova ocupacao nao ultrapassa a capacidade do cinema.
7. O sistema grava o registro em SQLite.
8. O sistema apresenta a ocupacao atualizada.
