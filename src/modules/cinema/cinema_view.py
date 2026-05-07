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
