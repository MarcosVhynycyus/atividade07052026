# Arquitetura

## Organizacao

A aplicacao segue MVC com duas camadas adicionais:

- View: imprime dados e mensagens no terminal.
- Controller: recebe entradas, converte tipos simples e devolve respostas padronizadas.
- Service: aplica regras de negocio.
- Repository: executa consultas e comandos SQL.

## Entidades principais

- Cinema: unidade da rede, com endereco e capacidade.
- Filme: obra exibida, com genero, diretor, elenco, duracao e classificacao.
- Sessao: exibicao de um filme em um cinema, sala e horario.
- Publico: registro de quantidade de espectadores em uma sessao.

## Persistencia

O banco SQLite fica em `src/config/database.db`. O arquivo `init.py` cria as tabelas e insere dados iniciais para permitir testes imediatos.

## Caso de uso completo

O caso de uso completo implementado e "Registrar publico de uma sessao". Ele percorre as quatro camadas do modulo `publico`, consulta dados da sessao, aplica a regra de capacidade e persiste o registro.
