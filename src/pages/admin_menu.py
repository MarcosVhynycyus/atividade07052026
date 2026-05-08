class AdminMenuPage:
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
        self.usuario = None

    def exibir(self, usuario):
        self.usuario = usuario
        while True:
            self._cabecalho("MENU ADMINISTRATIVO")
            print("1 - Listar sessoes em cartaz")
            print("2 - Registrar publico de uma sessao")
            print("3 - Consultar totalizacoes de publico")
            print("4 - Listar filmes")
            print("5 - Listar cinemas")
            print("6 - Gerenciar cinemas")
            print("7 - Gerenciar filmes")
            print("8 - Gerenciar sessoes")
            print("9 - Gerenciar publico")
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
            elif opcao == "6":
                self._menu_cinemas()
            elif opcao == "7":
                self._menu_filmes()
            elif opcao == "8":
                self._menu_sessoes()
            elif opcao == "9":
                self._menu_publico()
            elif opcao == "0":
                print("\nEncerrando o sistema.")
                break
            else:
                print("\nOpcao invalida.")

            input("\nPressione Enter para continuar...")

    def _cabecalho(self, titulo):
        print("\n" + "=" * 72)
        print("SISTEMA REDE DE CINEMAS")
        print(f"{titulo} | {self.usuario['nome']} ({self.usuario['perfil']})")
        print("=" * 72)

    def _submenu(self, titulo, opcoes):
        while True:
            self._cabecalho(titulo)
            for chave, item in opcoes.items():
                print(f"{chave} - {item['label']}")
            print("0 - Voltar")
            opcao = input("\nEscolha uma opcao: ").strip()

            if opcao == "0":
                return

            item = opcoes.get(opcao)
            if item:
                item["handler"]()
            else:
                print("\nOpcao invalida.")

            input("\nPressione Enter para continuar...")

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

    def _menu_cinemas(self):
        self._submenu(
            "GERENCIAR CINEMAS",
            {
                "1": {"label": "Listar cinemas", "handler": self._listar_cinemas},
                "2": {"label": "Adicionar cinema", "handler": self._adicionar_cinema},
                "3": {"label": "Alterar cinema", "handler": self._alterar_cinema},
                "4": {"label": "Excluir cinema", "handler": self._excluir_cinema},
            },
        )

    def _adicionar_cinema(self):
        nome = input("Nome: ").strip()
        cidade = input("Cidade: ").strip()
        estado = input("Estado (UF): ").strip()
        endereco = input("Endereco: ").strip()
        capacidade = input("Capacidade: ").strip()
        response = self.cinema_controller.criar_cinema(
            self.usuario,
            nome,
            cidade,
            estado,
            endereco,
            capacidade,
        )
        self.cinema_view.exibir_resultado(response)

    def _alterar_cinema(self):
        self._listar_cinemas()
        cinema_id = input("\nID do cinema: ").strip()
        nome = input("Novo nome: ").strip()
        cidade = input("Nova cidade: ").strip()
        estado = input("Novo estado (UF): ").strip()
        endereco = input("Novo endereco: ").strip()
        capacidade = input("Nova capacidade: ").strip()
        response = self.cinema_controller.atualizar_cinema(
            self.usuario,
            cinema_id,
            nome,
            cidade,
            estado,
            endereco,
            capacidade,
        )
        self.cinema_view.exibir_resultado(response)

    def _excluir_cinema(self):
        self._listar_cinemas()
        cinema_id = input("\nID do cinema: ").strip()
        if not self._confirmar_exclusao("cinema"):
            return
        response = self.cinema_controller.excluir_cinema(self.usuario, cinema_id)
        self.cinema_view.exibir_resultado(response)

    def _menu_filmes(self):
        self._submenu(
            "GERENCIAR FILMES",
            {
                "1": {"label": "Listar filmes", "handler": self._listar_filmes},
                "2": {"label": "Adicionar filme", "handler": self._adicionar_filme},
                "3": {"label": "Alterar filme", "handler": self._alterar_filme},
                "4": {"label": "Excluir filme", "handler": self._excluir_filme},
            },
        )

    def _adicionar_filme(self):
        titulo = input("Titulo: ").strip()
        genero = input("Genero: ").strip()
        diretor = input("Diretor: ").strip()
        elenco = input("Elenco: ").strip()
        duracao = input("Duracao em minutos: ").strip()
        classificacao = input("Classificacao: ").strip()
        response = self.filme_controller.criar_filme(
            self.usuario,
            titulo,
            genero,
            diretor,
            elenco,
            duracao,
            classificacao,
        )
        self.filme_view.exibir_resultado(response)

    def _alterar_filme(self):
        self._listar_filmes()
        filme_id = input("\nID do filme: ").strip()
        titulo = input("Novo titulo: ").strip()
        genero = input("Novo genero: ").strip()
        diretor = input("Novo diretor: ").strip()
        elenco = input("Novo elenco: ").strip()
        duracao = input("Nova duracao em minutos: ").strip()
        classificacao = input("Nova classificacao: ").strip()
        response = self.filme_controller.atualizar_filme(
            self.usuario,
            filme_id,
            titulo,
            genero,
            diretor,
            elenco,
            duracao,
            classificacao,
        )
        self.filme_view.exibir_resultado(response)

    def _excluir_filme(self):
        self._listar_filmes()
        filme_id = input("\nID do filme: ").strip()
        if not self._confirmar_exclusao("filme"):
            return
        response = self.filme_controller.excluir_filme(self.usuario, filme_id)
        self.filme_view.exibir_resultado(response)

    def _menu_sessoes(self):
        self._submenu(
            "GERENCIAR SESSOES",
            {
                "1": {"label": "Listar sessoes", "handler": self._listar_sessoes},
                "2": {"label": "Adicionar sessao", "handler": self._adicionar_sessao},
                "3": {"label": "Alterar sessao", "handler": self._alterar_sessao},
                "4": {"label": "Excluir sessao", "handler": self._excluir_sessao},
            },
        )

    def _adicionar_sessao(self):
        self._listar_cinemas()
        self._listar_filmes()
        cinema_id = input("\nID do cinema: ").strip()
        filme_id = input("ID do filme: ").strip()
        sala = input("Sala: ").strip()
        inicio = input("Inicio (AAAA-MM-DD HH:MM): ").strip()
        intervalo = input("Intervalo em minutos: ").strip()
        response = self.sessao_controller.criar_sessao(
            self.usuario,
            cinema_id,
            filme_id,
            sala,
            inicio,
            intervalo,
        )
        self.sessao_view.exibir_resultado(response)

    def _alterar_sessao(self):
        self._listar_sessoes()
        self._listar_cinemas()
        self._listar_filmes()
        sessao_id = input("\nID da sessao: ").strip()
        cinema_id = input("Novo ID do cinema: ").strip()
        filme_id = input("Novo ID do filme: ").strip()
        sala = input("Nova sala: ").strip()
        inicio = input("Novo inicio (AAAA-MM-DD HH:MM): ").strip()
        intervalo = input("Novo intervalo em minutos: ").strip()
        response = self.sessao_controller.atualizar_sessao(
            self.usuario,
            sessao_id,
            cinema_id,
            filme_id,
            sala,
            inicio,
            intervalo,
        )
        self.sessao_view.exibir_resultado(response)

    def _excluir_sessao(self):
        self._listar_sessoes()
        sessao_id = input("\nID da sessao: ").strip()
        if not self._confirmar_exclusao("sessao"):
            return
        response = self.sessao_controller.excluir_sessao(self.usuario, sessao_id)
        self.sessao_view.exibir_resultado(response)

    def _menu_publico(self):
        self._submenu(
            "GERENCIAR PUBLICO",
            {
                "1": {"label": "Listar registros", "handler": self._listar_publicos},
                "2": {"label": "Registrar publico", "handler": self._registrar_publico},
                "3": {"label": "Alterar registro", "handler": self._alterar_publico},
                "4": {"label": "Excluir registro", "handler": self._excluir_publico},
            },
        )

    def _listar_publicos(self):
        response = self.publico_controller.listar_publicos(self.usuario)
        if not response["ok"]:
            self.publico_view.exibir_resultado_admin(response)
            return
        self.publico_view.exibir_publicos(response["data"])

    def _alterar_publico(self):
        self._listar_publicos()
        self._listar_sessoes()
        publico_id = input("\nID do registro de publico: ").strip()
        sessao_id = input("Novo ID da sessao: ").strip()
        data_registro = input("Nova data de registro (AAAA-MM-DD): ").strip()
        quantidade = input("Nova quantidade: ").strip()
        response = self.publico_controller.atualizar_publico(
            self.usuario,
            publico_id,
            sessao_id,
            data_registro,
            quantidade,
        )
        self.publico_view.exibir_resultado_admin(response)

    def _excluir_publico(self):
        self._listar_publicos()
        publico_id = input("\nID do registro de publico: ").strip()
        if not self._confirmar_exclusao("registro de publico"):
            return
        response = self.publico_controller.excluir_publico(self.usuario, publico_id)
        self.publico_view.exibir_resultado_admin(response)

    def _confirmar_exclusao(self, entidade):
        confirmacao = input(f"Digite EXCLUIR para confirmar a exclusao de {entidade}: ")
        if confirmacao.strip().upper() == "EXCLUIR":
            return True
        print("\nExclusao cancelada.")
        return False
