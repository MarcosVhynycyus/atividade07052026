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

    def listar_publicos(self, usuario):
        try:
            return {"ok": True, "data": self.service.listar_publicos(usuario)}
        except (ValueError, PermissionError) as error:
            return {"ok": False, "erro": str(error)}

    def atualizar_publico(
        self,
        usuario,
        publico_id,
        sessao_id,
        data_registro,
        quantidade,
    ):
        try:
            publico_id_convertido = int(publico_id)
            sessao_id_convertido = int(sessao_id)
            quantidade_convertida = int(quantidade)
            data = self.service.atualizar_publico(
                usuario,
                publico_id_convertido,
                sessao_id_convertido,
                data_registro,
                quantidade_convertida,
            )
            return {
                "ok": True,
                "data": data,
                "mensagem": "Registro de publico atualizado com sucesso.",
            }
        except (ValueError, PermissionError) as error:
            return {"ok": False, "erro": str(error)}

    def excluir_publico(self, usuario, publico_id):
        try:
            publico_id_convertido = int(publico_id)
            self.service.excluir_publico(usuario, publico_id_convertido)
            return {
                "ok": True,
                "data": {"id": publico_id_convertido},
                "mensagem": "Registro de publico excluido com sucesso.",
            }
        except (ValueError, PermissionError) as error:
            return {"ok": False, "erro": str(error)}
