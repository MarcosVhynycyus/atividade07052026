from src.config.conn import get_connection


class CinemaRepository:
    def listar(self):
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT id, nome, cidade, estado, endereco, capacidade
                FROM cinemas
                ORDER BY nome
                """
            ).fetchall()
        return [dict(row) for row in rows]
