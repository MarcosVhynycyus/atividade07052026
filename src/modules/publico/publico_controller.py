class PublicoController:
    def __init__(self, service):
        self.service = service

    def registrar_publico(self, sessao_id, quantidade):
        try:
            sessao_id_convertido = int(sessao_id)
            quantidade_convertida = int(quantidade)
            data = self.service.registrar_publico(
                sessao_id_convertido,
                quantidade_convertida,
            )
            return {"ok": True, "data": data}
        except ValueError as error:
            return {"ok": False, "erro": str(error)}
