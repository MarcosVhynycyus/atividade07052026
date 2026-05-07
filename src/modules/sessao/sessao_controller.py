class SessaoController:
    def __init__(self, service):
        self.service = service

    def listar_sessoes(self):
        return {"ok": True, "data": self.service.listar_sessoes()}
