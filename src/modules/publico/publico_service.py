from datetime import date, datetime


class PublicoService:
    def __init__(self, repository):
        self.repository = repository

    def registrar_publico(self, sessao_id, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade de espectadores deve ser maior que zero.")

        sessao = self.repository.obter_sessao_com_publico(sessao_id)
        if not sessao:
            raise ValueError("Sessao nao encontrada.")

        novo_total = sessao["publico_registrado"] + quantidade
        if novo_total > sessao["capacidade"]:
            restantes = sessao["capacidade"] - sessao["publico_registrado"]
            raise ValueError(
                "Capacidade excedida. "
                f"A sessao ainda comporta {max(restantes, 0)} espectadores."
            )

        registro_id = self.repository.registrar_publico(
            sessao_id=sessao_id,
            data_registro=date.today().isoformat(),
            quantidade=quantidade,
        )

        return {
            "registro_id": registro_id,
            "sessao_id": sessao_id,
            "filme": sessao["filme"],
            "cinema": sessao["cinema"],
            "sala": sessao["sala"],
            "inicio": sessao["inicio"],
            "quantidade_registrada": quantidade,
            "publico_total": novo_total,
            "capacidade": sessao["capacidade"],
            "lugares_restantes": sessao["capacidade"] - novo_total,
        }

    def listar_publicos(self, usuario):
        self._autorizar_admin(usuario)
        return self.repository.listar()

    def atualizar_publico(
        self,
        usuario,
        publico_id,
        sessao_id,
        data_registro,
        quantidade,
    ):
        self._autorizar_admin(usuario)
        if quantidade <= 0:
            raise ValueError("A quantidade de espectadores deve ser maior que zero.")

        registro = self.repository.obter_por_id(publico_id)
        if not registro:
            raise ValueError("Registro de publico nao encontrado.")

        data_registro = self._validar_data(data_registro)
        sessao = self.repository.obter_sessao_com_publico(sessao_id, publico_id)
        if not sessao:
            raise ValueError("Sessao nao encontrada.")

        novo_total = sessao["publico_registrado"] + quantidade
        if novo_total > sessao["capacidade"]:
            restantes = sessao["capacidade"] - sessao["publico_registrado"]
            raise ValueError(
                "Capacidade excedida. "
                f"A sessao ainda comporta {max(restantes, 0)} espectadores."
            )

        self.repository.atualizar_publico(
            publico_id,
            sessao_id,
            data_registro,
            quantidade,
        )

        return {
            "id": publico_id,
            "sessao_id": sessao_id,
            "filme": sessao["filme"],
            "cinema": sessao["cinema"],
            "sala": sessao["sala"],
            "inicio": sessao["inicio"],
            "data_registro": data_registro,
            "quantidade": quantidade,
            "publico_total": novo_total,
            "capacidade": sessao["capacidade"],
            "lugares_restantes": sessao["capacidade"] - novo_total,
        }

    def excluir_publico(self, usuario, publico_id):
        self._autorizar_admin(usuario)
        if not self.repository.obter_por_id(publico_id):
            raise ValueError("Registro de publico nao encontrado.")
        self.repository.excluir_publico(publico_id)

    def _autorizar_admin(self, usuario):
        if not usuario or usuario.get("perfil") != "admin":
            raise PermissionError("Apenas administradores podem executar esta operacao.")

    def _validar_data(self, data_registro):
        data_registro = (data_registro or "").strip()
        try:
            datetime.strptime(data_registro, "%Y-%m-%d")
        except ValueError as error:
            raise ValueError("Data de registro deve estar no formato AAAA-MM-DD.") from error
        return data_registro
