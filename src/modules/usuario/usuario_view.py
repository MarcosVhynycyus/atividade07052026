class UsuarioView:
    def solicitar_credenciais(self):
        print("\nLOGIN")
        print("-" * 72)
        print("Informe 0 no login para sair.")
        login = input("Login: ").strip()
        if login == "0":
            return None
        senha = input("Senha: ").strip()
        return {"login": login, "senha": senha}

    def exibir_erro(self, erro):
        print(f"\nErro: {erro}")
