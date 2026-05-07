from src.config.conn import get_connection


class PublicoRepository:
    def obter_sessao_com_publico(self, sessao_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT
                    s.id,
                    s.sala,
                    s.inicio,
                    c.nome AS cinema,
                    c.capacidade,
                    f.titulo AS filme,
                    COALESCE(SUM(p.quantidade), 0) AS publico_registrado
                FROM sessoes s
                JOIN cinemas c ON c.id = s.cinema_id
                JOIN filmes f ON f.id = s.filme_id
                LEFT JOIN publicos p ON p.sessao_id = s.id
                WHERE s.id = ?
                GROUP BY s.id
                """,
                (sessao_id,),
            ).fetchone()
        return dict(row) if row else None

    def registrar_publico(self, sessao_id, data_registro, quantidade):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO publicos (sessao_id, data_registro, quantidade)
                VALUES (?, ?, ?)
                """,
                (sessao_id, data_registro, quantidade),
            )
            connection.commit()
            return cursor.lastrowid
