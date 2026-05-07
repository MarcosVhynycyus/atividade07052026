from src.config.conn import get_connection


class FilmeRepository:
    def listar(self):
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT id, titulo, genero, diretor, elenco, duracao_minutos, classificacao
                FROM filmes
                ORDER BY titulo
                """
            ).fetchall()
        return [dict(row) for row in rows]
