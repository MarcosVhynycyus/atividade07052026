# Rede de Cinemas - Requisitos e Regras de Negocio

## Escopo

Sistema enxuto para centralizar filmes, cinemas, sessoes, registros de publico e usuarios de uma rede de cinemas. A nova versao separa os perfis de administrador e staff: o staff conserva as funcoes operacionais ja existentes, enquanto o administrador tambem pode manter os cadastros da aplicacao.

## Atores

- Administrador: mantem cinemas, filmes, sessoes, registros de publico e consulta a operacao.
- Staff: registra publico, consulta sessoes, filmes, cinemas e totalizacoes.
- Espectador: consulta filmes, sessoes e informacoes basicas de exibicao.

## Requisitos funcionais

- RF01 - Listar cinemas cadastrados, com cidade, estado, endereco e capacidade.
- RF02 - Listar filmes em cartaz, com genero, diretor, elenco, classificacao e duracao.
- RF03 - Listar sessoes por cinema, filme, sala, horario e ocupacao atual.
- RF04 - Registrar o publico de uma sessao.
- RF05 - Totalizar publico por sessao, por filme e por cinema.
- RF06 - Consultar informacoes de filmes, incluindo genero, diretor e elenco.
- RF07 - Autenticar usuarios por login e senha.
- RF08 - Autorizar funcionalidades conforme o perfil do usuario autenticado.
- RF09 - Permitir que o administrador adicione, altere e exclua cinemas.
- RF10 - Permitir que o administrador adicione, altere e exclua filmes.
- RF11 - Permitir que o administrador adicione, altere e exclua sessoes.
- RF12 - Permitir que o administrador liste, altere e exclua registros de publico.

## Requisitos nao funcionais

- RNF01 - A aplicacao deve persistir dados em SQLite.
- RNF02 - A arquitetura deve separar View, Controller, Service e Repository.
- RNF03 - A interface deve ser simples e executada em terminal.
- RNF04 - O sistema deve permitir evolucao de entidades sem alterar todas as camadas.
- RNF05 - As regras de negocio devem ficar concentradas nos services.
- RNF06 - As credenciais devem ser persistidas em SQLite com senha armazenada em hash.
- RNF07 - A autorizacao deve ser validada na camada de service, alem da separacao visual dos menus.
- RNF08 - A inicializacao deve criar estruturas novas sem apagar dados existentes.

## Regras de negocio

- RN01 - Uma sessao pertence a um cinema e exibe um unico filme.
- RN02 - Um cinema pode possuir varias sessoes.
- RN03 - Um filme pode estar em varias sessoes e em diferentes cinemas.
- RN04 - O publico registrado em uma sessao nao pode ultrapassar a capacidade do cinema.
- RN05 - O registro de publico deve ter quantidade inteira positiva.
- RN06 - A totalizacao de publico por filme soma todos os registros das sessoes daquele filme.
- RN07 - A totalizacao de publico por cinema soma todos os registros das sessoes daquele cinema.
- RN08 - A organizacao das sessoes deve considerar a duracao do filme e o intervalo minimo cadastrado entre exibicoes.
- RN09 - Apenas usuarios ativos e com senha valida podem acessar a aplicacao.
- RN10 - Apenas usuarios com perfil admin podem criar, alterar ou excluir cinemas, filmes, sessoes e registros de publico.
- RN11 - Usuarios com perfil staff podem executar somente as funcoes basicas da versao anterior.
- RN12 - Cinemas e filmes com sessoes vinculadas nao podem ser excluidos.
- RN13 - Sessoes com registros de publico vinculados nao podem ser excluidas.
- RN14 - Alteracoes em registros de publico tambem devem respeitar a capacidade do cinema da sessao.
- RN15 - Alteracoes em cinemas ou sessoes nao podem deixar publico ja registrado acima da capacidade do cinema.

## Caso de uso implementado

Registrar publico de uma sessao:

1. O usuario autenticado como admin ou staff consulta as sessoes em cartaz.
2. O usuario informa o identificador da sessao.
3. O usuario informa a quantidade de espectadores da sessao.
4. O sistema valida se a sessao existe.
5. O sistema valida se a quantidade e positiva.
6. O sistema valida se a nova ocupacao nao ultrapassa a capacidade do cinema.
7. O sistema grava o registro em SQLite.
8. O sistema apresenta a ocupacao atualizada.
