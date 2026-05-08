class CinemaController:
    def __init__(self, service):
        self.service = service

    def listar_cinemas(self):
        return {"ok": True, "data": self.service.listar_cinemas()}

    def criar_cinema(self, usuario, nome, cidade, estado, endereco, capacidade):
        try:
            capacidade_convertida = int(capacidade)
            data = self.service.criar_cinema(
                usuario,
                nome,
                cidade,
                estado,
                endereco,
                capacidade_convertida,
            )
            return {
                "ok": True,
                "data": data,
                "mensagem": "Cinema cadastrado com sucesso.",
            }
        except (ValueError, PermissionError) as error:
            return {"ok": False, "erro": str(error)}

    def atualizar_cinema(self, usuario, cinema_id, nome, cidade, estado, endereco, capacidade):
        try:
            cinema_id_convertido = int(cinema_id)
            capacidade_convertida = int(capacidade)
            data = self.service.atualizar_cinema(
                usuario,
                cinema_id_convertido,
                nome,
                cidade,
                estado,
                endereco,
                capacidade_convertida,
            )
            return {
                "ok": True,
                "data": data,
                "mensagem": "Cinema atualizado com sucesso.",
            }
        except (ValueError, PermissionError) as error:
            return {"ok": False, "erro": str(error)}

    def excluir_cinema(self, usuario, cinema_id):
        try:
            cinema_id_convertido = int(cinema_id)
            self.service.excluir_cinema(usuario, cinema_id_convertido)
            return {
                "ok": True,
                "data": {"id": cinema_id_convertido},
                "mensagem": "Cinema excluido com sucesso.",
            }
        except (ValueError, PermissionError) as error:
            return {"ok": False, "erro": str(error)}
