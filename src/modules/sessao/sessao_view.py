class SessaoView:
    def exibir_sessoes(self, sessoes):
        print("\nSESSOES EM CARTAZ")
        print("-" * 72)
        if not sessoes:
            print("Nenhuma sessao cadastrada.")
            return

        for sessao in sessoes:
            print(
                f"[{sessao['id']}] {sessao['inicio']} | {sessao['cinema']} "
                f"({sessao['cidade']}/{sessao['estado']}) | {sessao['sala']}"
            )
            print(
                f"    Filme: {sessao['filme']} | Genero: {sessao['genero']} | "
                f"Duracao: {sessao['duracao_minutos']} min"
            )
            print(
                f"    Publico: {sessao['publico_registrado']}/{sessao['capacidade']} "
                f"| Lugares restantes: {sessao['lugares_restantes']}"
            )

    def exibir_resultado(self, response):
        print("\nOPERACAO DE SESSAO")
        print("-" * 72)
        if not response["ok"]:
            print(f"Erro: {response['erro']}")
            return

        print(response.get("mensagem", "Operacao realizada com sucesso."))
        sessao = response.get("data")
        if sessao and "inicio" in sessao:
            print(
                f"[{sessao['id']}] {sessao['inicio']} | {sessao['cinema']} | "
                f"{sessao['sala']} | {sessao['filme']}"
            )
