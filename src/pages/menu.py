class MenuPage:
    def __init__(
        self,
        sessao_controller,
        sessao_view,
        publico_controller,
        publico_view,
        relatorio_controller,
        relatorio_view,
        cinema_controller,
        cinema_view,
        filme_controller,
        filme_view,
    ):
        self.sessao_controller = sessao_controller
        self.sessao_view = sessao_view
        self.publico_controller = publico_controller
        self.publico_view = publico_view
        self.relatorio_controller = relatorio_controller
        self.relatorio_view = relatorio_view
        self.cinema_controller = cinema_controller
        self.cinema_view = cinema_view
        self.filme_controller = filme_controller
        self.filme_view = filme_view

    def exibir(self):
        while True:
            self._cabecalho()
            print("1 - Listar sessoes em cartaz")
            print("2 - Registrar publico de uma sessao")
            print("3 - Consultar totalizacoes de publico")
            print("4 - Listar filmes")
            print("5 - Listar cinemas")
            print("0 - Sair")
            opcao = input("\nEscolha uma opcao: ").strip()

            if opcao == "1":
                self._listar_sessoes()
            elif opcao == "2":
                self._registrar_publico()
            elif opcao == "3":
                self._consultar_totalizacoes()
            elif opcao == "4":
                self._listar_filmes()
            elif opcao == "5":
                self._listar_cinemas()
            elif opcao == "0":
                print("\nEncerrando o sistema.")
                break
            else:
                print("\nOpcao invalida.")

            input("\nPressione Enter para continuar...")

    def _cabecalho(self):
        print("\n" + "=" * 72)
        print("SISTEMA REDE DE CINEMAS")
        print("=" * 72)

    def _listar_sessoes(self):
        response = self.sessao_controller.listar_sessoes()
        self.sessao_view.exibir_sessoes(response["data"])

    def _registrar_publico(self):
        self._listar_sessoes()
        sessao_id = input("\nID da sessao: ").strip()
        quantidade = input("Quantidade de espectadores: ").strip()
        response = self.publico_controller.registrar_publico(sessao_id, quantidade)
        self.publico_view.exibir_resultado(response)

    def _consultar_totalizacoes(self):
        response = self.relatorio_controller.obter_totalizacoes()
        self.relatorio_view.exibir_totalizacoes(response["data"])

    def _listar_filmes(self):
        response = self.filme_controller.listar_filmes()
        self.filme_view.exibir_filmes(response["data"])

    def _listar_cinemas(self):
        response = self.cinema_controller.listar_cinemas()
        self.cinema_view.exibir_cinemas(response["data"])
