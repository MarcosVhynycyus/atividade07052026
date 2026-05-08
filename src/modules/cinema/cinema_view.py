class CinemaView:
    def exibir_cinemas(self, cinemas):
        print("\nCINEMAS CADASTRADOS")
        print("-" * 72)
        if not cinemas:
            print("Nenhum cinema cadastrado.")
            return

        for cinema in cinemas:
            print(
                f"[{cinema['id']}] {cinema['nome']} - {cinema['cidade']}/{cinema['estado']}"
            )
            print(f"    Endereco: {cinema['endereco']}")
            print(f"    Capacidade: {cinema['capacidade']} lugares")

    def exibir_resultado(self, response):
        print("\nOPERACAO DE CINEMA")
        print("-" * 72)
        if not response["ok"]:
            print(f"Erro: {response['erro']}")
            return

        print(response.get("mensagem", "Operacao realizada com sucesso."))
        cinema = response.get("data")
        if cinema and "nome" in cinema:
            print(
                f"[{cinema['id']}] {cinema['nome']} - "
                f"{cinema['cidade']}/{cinema['estado']}"
            )
