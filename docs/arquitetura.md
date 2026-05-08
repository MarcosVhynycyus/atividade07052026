# Arquitetura

## Organizacao

A aplicacao segue MVC com duas camadas adicionais:

- View: imprime dados e mensagens no terminal.
- Controller: recebe entradas, converte tipos simples e devolve respostas padronizadas.
- Service: aplica regras de negocio.
- Repository: executa consultas e comandos SQL.

O controle de acesso foi incluido sem quebrar essa separacao. A tela de login e os menus ficam em `pages`, a autenticacao fica no modulo `usuario`, e a autorizacao das operacoes administrativas e validada nos services dos modulos de dominio.

## Entidades principais

- Cinema: unidade da rede, com endereco e capacidade.
- Filme: obra exibida, com genero, diretor, elenco, duracao e classificacao.
- Sessao: exibicao de um filme em um cinema, sala e horario.
- Publico: registro de quantidade de espectadores em uma sessao.
- Usuario: credencial de acesso com perfil `admin` ou `staff`.

## Persistencia

O banco SQLite fica em `src/config/database.db`. O arquivo `init.py` cria as tabelas e insere dados iniciais para permitir testes imediatos. A inicializacao e executada a cada abertura da aplicacao para garantir que novas tabelas, como `usuarios`, sejam criadas em bancos ja existentes sem apagar dados.

Usuarios iniciais:

- Admin: login `admin`, senha `admin123`.
- Staff: login `staff`, senha `staff123`.

## Caso de uso completo

O caso de uso completo implementado e "Registrar publico de uma sessao". Ele percorre as quatro camadas do modulo `publico`, consulta dados da sessao, aplica a regra de capacidade e persiste o registro.

As operacoes administrativas seguem o mesmo caminho: `AdminMenuPage` coleta entradas, o controller converte tipos e padroniza respostas, o service valida perfil e regras de negocio, e o repository executa os comandos SQL.
