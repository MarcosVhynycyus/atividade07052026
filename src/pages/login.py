class LoginPage:
    def __init__(self, usuario_controller, usuario_view):
        self.usuario_controller = usuario_controller
        self.usuario_view = usuario_view

    def exibir(self):
        while True:
            credenciais = self.usuario_view.solicitar_credenciais()
            if credenciais is None:
                print("\nEncerrando o sistema.")
                return None

            response = self.usuario_controller.autenticar(
                credenciais["login"],
                credenciais["senha"],
            )
            if response["ok"]:
                return response["data"]

            self.usuario_view.exibir_erro(response["erro"])
            input("\nPressione Enter para tentar novamente...")
