import hashlib


class UsuarioService:
    def __init__(self, repository):
        self.repository = repository

    def autenticar(self, login, senha):
        login = self._validar_texto(login, "Login")
        senha = self._validar_texto(senha, "Senha")

        usuario = self.repository.buscar_por_login(login)
        if not usuario or usuario["senha_hash"] != self._gerar_hash(senha):
            raise ValueError("Login ou senha invalidos.")

        if not usuario["ativo"]:
            raise ValueError("Usuario inativo.")

        return {
            "id": usuario["id"],
            "nome": usuario["nome"],
            "login": usuario["login"],
            "perfil": usuario["perfil"],
        }

    def _validar_texto(self, valor, campo):
        valor = (valor or "").strip()
        if not valor:
            raise ValueError(f"{campo} e obrigatorio.")
        return valor

    def _gerar_hash(self, senha):
        return hashlib.sha256(senha.encode("utf-8")).hexdigest()
