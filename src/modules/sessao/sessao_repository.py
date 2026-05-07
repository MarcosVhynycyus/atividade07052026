from src.config.conn import get_connection


class SessaoRepository:
    def listar(self):
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT
                    s.id,
                    s.sala,
                    s.inicio,
                    s.intervalo_minutos,
                    c.nome AS cinema,
                    c.cidade,
                    c.estado,
                    c.capacidade,
                    f.titulo AS filme,
                    f.genero,
                    f.diretor,
                    f.duracao_minutos,
                    COALESCE(SUM(p.quantidade), 0) AS publico_registrado
                FROM sessoes s
                JOIN cinemas c ON c.id = s.cinema_id
                JOIN filmes f ON f.id = s.filme_id
                LEFT JOIN publicos p ON p.sessao_id = s.id
                GROUP BY s.id
                ORDER BY s.inicio, c.nome, s.sala
                """
            ).fetchall()
        return [dict(row) for row in rows]
