from src.config.conn import get_connection


class RelatorioRepository:
    def total_por_sessao(self):
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT
                    s.id AS sessao_id,
                    s.inicio,
                    c.nome AS cinema,
                    f.titulo AS filme,
                    COALESCE(SUM(p.quantidade), 0) AS total_publico
                FROM sessoes s
                JOIN cinemas c ON c.id = s.cinema_id
                JOIN filmes f ON f.id = s.filme_id
                LEFT JOIN publicos p ON p.sessao_id = s.id
                GROUP BY s.id
                ORDER BY s.inicio
                """
            ).fetchall()
        return [dict(row) for row in rows]

    def total_por_filme(self):
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT
                    f.id AS filme_id,
                    f.titulo AS filme,
                    COALESCE(SUM(p.quantidade), 0) AS total_publico
                FROM filmes f
                LEFT JOIN sessoes s ON s.filme_id = f.id
                LEFT JOIN publicos p ON p.sessao_id = s.id
                GROUP BY f.id
                ORDER BY total_publico DESC, f.titulo
                """
            ).fetchall()
        return [dict(row) for row in rows]

    def total_por_cinema(self):
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT
                    c.id AS cinema_id,
                    c.nome AS cinema,
                    c.cidade,
                    c.estado,
                    COALESCE(SUM(p.quantidade), 0) AS total_publico
                FROM cinemas c
                LEFT JOIN sessoes s ON s.cinema_id = c.id
                LEFT JOIN publicos p ON p.sessao_id = s.id
                GROUP BY c.id
                ORDER BY total_publico DESC, c.nome
                """
            ).fetchall()
        return [dict(row) for row in rows]
