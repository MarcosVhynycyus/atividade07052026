class FilmeService:
    def __init__(self, repository):
        self.repository = repository

    def listar_filmes(self):
        return self.repository.listar()
