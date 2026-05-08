class FilmeController:
    def __init__(self, service):
        self.service = service

    def listar_filmes(self):
        return {"ok": True, "data": self.service.listar_filmes()}

    def criar_filme(
        self,
        usuario,
        titulo,
        genero,
        diretor,
        elenco,
        duracao_minutos,
        classificacao,
    ):
        try:
            duracao_convertida = int(duracao_minutos)
            data = self.service.criar_filme(
                usuario,
                titulo,
                genero,
                diretor,
                elenco,
                duracao_convertida,
                classificacao,
            )
            return {
                "ok": True,
                "data": data,
                "mensagem": "Filme cadastrado com sucesso.",
            }
        except (ValueError, PermissionError) as error:
            return {"ok": False, "erro": str(error)}

    def atualizar_filme(
        self,
        usuario,
        filme_id,
        titulo,
        genero,
        diretor,
        elenco,
        duracao_minutos,
        classificacao,
    ):
        try:
            filme_id_convertido = int(filme_id)
            duracao_convertida = int(duracao_minutos)
            data = self.service.atualizar_filme(
                usuario,
                filme_id_convertido,
                titulo,
                genero,
                diretor,
                elenco,
                duracao_convertida,
                classificacao,
            )
            return {
                "ok": True,
                "data": data,
                "mensagem": "Filme atualizado com sucesso.",
            }
        except (ValueError, PermissionError) as error:
            return {"ok": False, "erro": str(error)}

    def excluir_filme(self, usuario, filme_id):
        try:
            filme_id_convertido = int(filme_id)
            self.service.excluir_filme(usuario, filme_id_convertido)
            return {
                "ok": True,
                "data": {"id": filme_id_convertido},
                "mensagem": "Filme excluido com sucesso.",
            }
        except (ValueError, PermissionError) as error:
            return {"ok": False, "erro": str(error)}
