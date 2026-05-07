class RelatorioService:
    def __init__(self, repository):
        self.repository = repository

    def obter_totalizacoes(self):
        return {
            "por_sessao": self.repository.total_por_sessao(),
            "por_filme": self.repository.total_por_filme(),
            "por_cinema": self.repository.total_por_cinema(),
        }
