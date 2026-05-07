class FilmeController:
    def __init__(self, service):
        self.service = service

    def listar_filmes(self):
        return {"ok": True, "data": self.service.listar_filmes()}
