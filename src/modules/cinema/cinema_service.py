class CinemaService:
    def __init__(self, repository):
        self.repository = repository

    def listar_cinemas(self):
        return self.repository.listar()
