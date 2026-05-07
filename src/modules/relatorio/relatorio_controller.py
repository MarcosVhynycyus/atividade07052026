class RelatorioController:
    def __init__(self, service):
        self.service = service

    def obter_totalizacoes(self):
        return {"ok": True, "data": self.service.obter_totalizacoes()}
