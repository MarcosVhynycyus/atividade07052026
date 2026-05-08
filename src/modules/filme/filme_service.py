class FilmeService:
    def __init__(self, repository):
        self.repository = repository

    def listar_filmes(self):
        return self.repository.listar()

    def criar_filme(
        self,
        usuario,
        titulo,
        genero,
        diretor,
        elenco,
        duracao_minutos,
        classificacao,
    ):
        self._autorizar_admin(usuario)
        titulo = self._validar_texto(titulo, "Titulo")
        genero = self._validar_texto(genero, "Genero")
        diretor = self._validar_texto(diretor, "Diretor")
        elenco = self._validar_texto(elenco, "Elenco")
        duracao_minutos = self._validar_inteiro_positivo(
            duracao_minutos,
            "Duracao",
        )
        classificacao = self._validar_texto(classificacao, "Classificacao")
        return self.repository.criar(
            titulo,
            genero,
            diretor,
            elenco,
            duracao_minutos,
            classificacao,
        )

    def atualizar_filme(
        self,
        usuario,
        filme_id,
        titulo,
        genero,
        diretor,
        elenco,
        duracao_minutos,
        classificacao,
    ):
        self._autorizar_admin(usuario)
        if not self.repository.obter_por_id(filme_id):
            raise ValueError("Filme nao encontrado.")

        titulo = self._validar_texto(titulo, "Titulo")
        genero = self._validar_texto(genero, "Genero")
        diretor = self._validar_texto(diretor, "Diretor")
        elenco = self._validar_texto(elenco, "Elenco")
        duracao_minutos = self._validar_inteiro_positivo(
            duracao_minutos,
            "Duracao",
        )
        classificacao = self._validar_texto(classificacao, "Classificacao")
        self.repository.atualizar(
            filme_id,
            titulo,
            genero,
            diretor,
            elenco,
            duracao_minutos,
            classificacao,
        )
        return self.repository.obter_por_id(filme_id)

    def excluir_filme(self, usuario, filme_id):
        self._autorizar_admin(usuario)
        if not self.repository.obter_por_id(filme_id):
            raise ValueError("Filme nao encontrado.")
        if self.repository.possui_sessoes(filme_id):
            raise ValueError("Filme possui sessoes vinculadas e nao pode ser excluido.")
        self.repository.excluir(filme_id)

    def _autorizar_admin(self, usuario):
        if not usuario or usuario.get("perfil") != "admin":
            raise PermissionError("Apenas administradores podem executar esta operacao.")

    def _validar_texto(self, valor, campo):
        valor = (valor or "").strip()
        if not valor:
            raise ValueError(f"{campo} e obrigatorio.")
        return valor

    def _validar_inteiro_positivo(self, valor, campo):
        if valor <= 0:
            raise ValueError(f"{campo} deve ser maior que zero.")
        return valor
