class CinemaService:
    def __init__(self, repository):
        self.repository = repository

    def listar_cinemas(self):
        return self.repository.listar()

    def criar_cinema(self, usuario, nome, cidade, estado, endereco, capacidade):
        self._autorizar_admin(usuario)
        nome = self._validar_texto(nome, "Nome")
        cidade = self._validar_texto(cidade, "Cidade")
        estado = self._validar_estado(estado)
        endereco = self._validar_texto(endereco, "Endereco")
        capacidade = self._validar_inteiro_positivo(capacidade, "Capacidade")
        return self.repository.criar(nome, cidade, estado, endereco, capacidade)

    def atualizar_cinema(self, usuario, cinema_id, nome, cidade, estado, endereco, capacidade):
        self._autorizar_admin(usuario)
        if not self.repository.obter_por_id(cinema_id):
            raise ValueError("Cinema nao encontrado.")

        nome = self._validar_texto(nome, "Nome")
        cidade = self._validar_texto(cidade, "Cidade")
        estado = self._validar_estado(estado)
        endereco = self._validar_texto(endereco, "Endereco")
        capacidade = self._validar_inteiro_positivo(capacidade, "Capacidade")
        maior_publico = self.repository.maior_publico_por_sessao(cinema_id)
        if capacidade < maior_publico:
            raise ValueError(
                "Capacidade menor que o publico ja registrado em uma sessao "
                f"do cinema ({maior_publico})."
            )
        self.repository.atualizar(cinema_id, nome, cidade, estado, endereco, capacidade)
        return self.repository.obter_por_id(cinema_id)

    def excluir_cinema(self, usuario, cinema_id):
        self._autorizar_admin(usuario)
        if not self.repository.obter_por_id(cinema_id):
            raise ValueError("Cinema nao encontrado.")
        if self.repository.possui_sessoes(cinema_id):
            raise ValueError("Cinema possui sessoes vinculadas e nao pode ser excluido.")
        self.repository.excluir(cinema_id)

    def _autorizar_admin(self, usuario):
        if not usuario or usuario.get("perfil") != "admin":
            raise PermissionError("Apenas administradores podem executar esta operacao.")

    def _validar_texto(self, valor, campo):
        valor = (valor or "").strip()
        if not valor:
            raise ValueError(f"{campo} e obrigatorio.")
        return valor

    def _validar_estado(self, estado):
        estado = self._validar_texto(estado, "Estado").upper()
        if len(estado) != 2:
            raise ValueError("Estado deve conter a sigla com 2 caracteres.")
        return estado

    def _validar_inteiro_positivo(self, valor, campo):
        if valor <= 0:
            raise ValueError(f"{campo} deve ser maior que zero.")
        return valor
