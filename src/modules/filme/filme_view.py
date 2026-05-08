class FilmeView:
    def exibir_filmes(self, filmes):
        print("\nFILMES EM CARTAZ")
        print("-" * 72)
        if not filmes:
            print("Nenhum filme cadastrado.")
            return

        for filme in filmes:
            print(f"[{filme['id']}] {filme['titulo']} ({filme['classificacao']})")
            print(
                f"    Genero: {filme['genero']} | Diretor: {filme['diretor']} | "
                f"Duracao: {filme['duracao_minutos']} min"
            )
            print(f"    Elenco: {filme['elenco']}")

    def exibir_resultado(self, response):
        print("\nOPERACAO DE FILME")
        print("-" * 72)
        if not response["ok"]:
            print(f"Erro: {response['erro']}")
            return

        print(response.get("mensagem", "Operacao realizada com sucesso."))
        filme = response.get("data")
        if filme and "titulo" in filme:
            print(f"[{filme['id']}] {filme['titulo']} ({filme['classificacao']})")
