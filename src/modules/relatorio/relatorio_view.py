class RelatorioView:
    def exibir_totalizacoes(self, totalizacoes):
        print("\nTOTALIZACOES DE PUBLICO")
        print("-" * 72)
        self._exibir_por_sessao(totalizacoes["por_sessao"])
        self._exibir_por_filme(totalizacoes["por_filme"])
        self._exibir_por_cinema(totalizacoes["por_cinema"])

    def _exibir_por_sessao(self, linhas):
        print("\nPor sessao")
        for linha in linhas:
            print(
                f"  Sessao {linha['sessao_id']} | {linha['inicio']} | "
                f"{linha['filme']} | {linha['cinema']}: {linha['total_publico']}"
            )

    def _exibir_por_filme(self, linhas):
        print("\nPor filme")
        for linha in linhas:
            print(f"  {linha['filme']}: {linha['total_publico']}")

    def _exibir_por_cinema(self, linhas):
        print("\nPor cinema")
        for linha in linhas:
            print(
                f"  {linha['cinema']} ({linha['cidade']}/{linha['estado']}): "
                f"{linha['total_publico']}"
            )
