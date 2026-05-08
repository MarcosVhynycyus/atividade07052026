from src.config.conn import get_connection


class UsuarioRepository:
    def buscar_por_login(self, login):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT id, nome, login, senha_hash, perfil, ativo
                FROM usuarios
                WHERE login = ?
                """,
                (login,),
            ).fetchone()
        return dict(row) if row else None
