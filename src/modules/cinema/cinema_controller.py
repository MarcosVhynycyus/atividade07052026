class CinemaController:
    def __init__(self, service):
        self.service = service

    def listar_cinemas(self):
        return {"ok": True, "data": self.service.listar_cinemas()}
