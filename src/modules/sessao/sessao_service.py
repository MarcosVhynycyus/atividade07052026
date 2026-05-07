class SessaoService:
    def __init__(self, repository):
        self.repository = repository

    def listar_sessoes(self):
        sessoes = self.repository.listar()
        for sessao in sessoes:
            sessao["lugares_restantes"] = (
                sessao["capacidade"] - sessao["publico_registrado"]
            )
        return sessoes
