class SessaoController:
    def __init__(self, service):
        self.service = service

    def listar_sessoes(self):
        return {"ok": True, "data": self.service.listar_sessoes()}

    def criar_sessao(
        self,
        usuario,
        cinema_id,
        filme_id,
        sala,
        inicio,
        intervalo_minutos,
    ):
        try:
            cinema_id_convertido = int(cinema_id)
            filme_id_convertido = int(filme_id)
            intervalo_convertido = int(intervalo_minutos)
            data = self.service.criar_sessao(
                usuario,
                cinema_id_convertido,
                filme_id_convertido,
                sala,
                inicio,
                intervalo_convertido,
            )
            return {
                "ok": True,
                "data": data,
                "mensagem": "Sessao cadastrada com sucesso.",
            }
        except (ValueError, PermissionError) as error:
            return {"ok": False, "erro": str(error)}

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
        try:
            sessao_id_convertido = int(sessao_id)
            cinema_id_convertido = int(cinema_id)
            filme_id_convertido = int(filme_id)
            intervalo_convertido = int(intervalo_minutos)
            data = self.service.atualizar_sessao(
                usuario,
                sessao_id_convertido,
                cinema_id_convertido,
                filme_id_convertido,
                sala,
                inicio,
                intervalo_convertido,
            )
            return {
                "ok": True,
                "data": data,
                "mensagem": "Sessao atualizada com sucesso.",
            }
        except (ValueError, PermissionError) as error:
            return {"ok": False, "erro": str(error)}

    def excluir_sessao(self, usuario, sessao_id):
        try:
            sessao_id_convertido = int(sessao_id)
            self.service.excluir_sessao(usuario, sessao_id_convertido)
            return {
                "ok": True,
                "data": {"id": sessao_id_convertido},
                "mensagem": "Sessao excluida com sucesso.",
            }
        except (ValueError, PermissionError) as error:
            return {"ok": False, "erro": str(error)}
