from datetime import date


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
