from datetime import datetime


class SessaoService:
    def __init__(self, repository):
        self.repository = repository

    def listar_sessoes(self):
        sessoes = self.repository.listar()
        for sessao in sessoes:
            sessao["lugares_restantes"] = (
                sessao["capacidade"] - sessao["publico_registrado"]
            )
        return sessoes

    def criar_sessao(
        self,
        usuario,
        cinema_id,
        filme_id,
        sala,
        inicio,
        intervalo_minutos,
    ):
        self._autorizar_admin(usuario)
        self._validar_relacionamentos(cinema_id, filme_id)
        sala = self._validar_texto(sala, "Sala")
        inicio = self._validar_inicio(inicio)
        intervalo_minutos = self._validar_inteiro_nao_negativo(
            intervalo_minutos,
            "Intervalo",
        )
        self._validar_conflito(cinema_id, sala, inicio)
        return self.repository.criar(
            cinema_id,
            filme_id,
            sala,
            inicio,
            intervalo_minutos,
        )

    def atualizar_sessao(
        self,
        usuario,
        sessao_id,
        cinema_id,
        filme_id,
        sala,
        inicio,
        intervalo_minutos,
    ):
        self._autorizar_admin(usuario)
        if not self.repository.obter_por_id(sessao_id):
            raise ValueError("Sessao nao encontrada.")

        self._validar_relacionamentos(cinema_id, filme_id)
        self._validar_publico_cabe_na_capacidade(sessao_id, cinema_id)
        sala = self._validar_texto(sala, "Sala")
        inicio = self._validar_inicio(inicio)
        intervalo_minutos = self._validar_inteiro_nao_negativo(
            intervalo_minutos,
            "Intervalo",
        )
        self._validar_conflito(cinema_id, sala, inicio, sessao_id)
        self.repository.atualizar(
            sessao_id,
            cinema_id,
            filme_id,
            sala,
            inicio,
            intervalo_minutos,
        )
        return self.repository.obter_por_id(sessao_id)

    def excluir_sessao(self, usuario, sessao_id):
        self._autorizar_admin(usuario)
        if not self.repository.obter_por_id(sessao_id):
            raise ValueError("Sessao nao encontrada.")
        if self.repository.possui_publico(sessao_id):
            raise ValueError("Sessao possui publico registrado e nao pode ser excluida.")
        self.repository.excluir(sessao_id)

    def _autorizar_admin(self, usuario):
        if not usuario or usuario.get("perfil") != "admin":
            raise PermissionError("Apenas administradores podem executar esta operacao.")

    def _validar_relacionamentos(self, cinema_id, filme_id):
        if not self.repository.cinema_existe(cinema_id):
            raise ValueError("Cinema nao encontrado.")
        if not self.repository.filme_existe(filme_id):
            raise ValueError("Filme nao encontrado.")

    def _validar_publico_cabe_na_capacidade(self, sessao_id, cinema_id):
        total_publico = self.repository.obter_total_publico(sessao_id)
        capacidade = self.repository.obter_capacidade_cinema(cinema_id)
        if capacidade is not None and total_publico > capacidade:
            raise ValueError(
                "A sessao possui publico registrado acima da capacidade "
                "do cinema informado."
            )

    def _validar_texto(self, valor, campo):
        valor = (valor or "").strip()
        if not valor:
            raise ValueError(f"{campo} e obrigatorio.")
        return valor

    def _validar_inicio(self, inicio):
        inicio = self._validar_texto(inicio, "Inicio")
        try:
            datetime.strptime(inicio, "%Y-%m-%d %H:%M")
        except ValueError as error:
            raise ValueError("Inicio deve estar no formato AAAA-MM-DD HH:MM.") from error
        return inicio

    def _validar_inteiro_nao_negativo(self, valor, campo):
        if valor < 0:
            raise ValueError(f"{campo} deve ser maior ou igual a zero.")
        return valor

    def _validar_conflito(
        self,
        cinema_id,
        sala,
        inicio,
        ignorar_sessao_id=None,
    ):
        if self.repository.existe_conflito(
            cinema_id,
            sala,
            inicio,
            ignorar_sessao_id,
        ):
            raise ValueError("Ja existe sessao para este cinema, sala e horario.")
