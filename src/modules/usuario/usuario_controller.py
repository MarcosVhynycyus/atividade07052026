class UsuarioController:
    def __init__(self, service):
        self.service = service

    def autenticar(self, login, senha):
        try:
            data = self.service.autenticar(login, senha)
            return {"ok": True, "data": data}
        except ValueError as error:
            return {"ok": False, "erro": str(error)}
