from src.config.conn import get_connection


class PublicoRepository:
    def listar(self):
        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT
                    p.id,
                    p.sessao_id,
                    p.data_registro,
                    p.quantidade,
                    p.criado_em,
                    s.inicio,
                    s.sala,
                    c.nome AS cinema,
                    f.titulo AS filme
                FROM publicos p
                JOIN sessoes s ON s.id = p.sessao_id
                JOIN cinemas c ON c.id = s.cinema_id
                JOIN filmes f ON f.id = s.filme_id
                ORDER BY p.criado_em DESC, p.id DESC
                """
            ).fetchall()
        return [dict(row) for row in rows]

    def obter_por_id(self, publico_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT
                    p.id,
                    p.sessao_id,
                    p.data_registro,
                    p.quantidade,
                    p.criado_em,
                    s.inicio,
                    s.sala,
                    c.nome AS cinema,
                    f.titulo AS filme
                FROM publicos p
                JOIN sessoes s ON s.id = p.sessao_id
                JOIN cinemas c ON c.id = s.cinema_id
                JOIN filmes f ON f.id = s.filme_id
                WHERE p.id = ?
                """,
                (publico_id,),
            ).fetchone()
        return dict(row) if row else None

    def obter_sessao_com_publico(self, sessao_id, ignorar_publico_id=None):
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
                LEFT JOIN publicos p
                    ON p.sessao_id = s.id
                   AND (? IS NULL OR p.id <> ?)
                WHERE s.id = ?
                GROUP BY s.id
                """,
                (ignorar_publico_id, ignorar_publico_id, sessao_id),
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

    def atualizar_publico(self, publico_id, sessao_id, data_registro, quantidade):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                UPDATE publicos
                SET sessao_id = ?,
                    data_registro = ?,
                    quantidade = ?
                WHERE id = ?
                """,
                (sessao_id, data_registro, quantidade, publico_id),
            )
            connection.commit()
            return cursor.rowcount

    def excluir_publico(self, publico_id):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                DELETE FROM publicos
                WHERE id = ?
                """,
                (publico_id,),
            )
            connection.commit()
            return cursor.rowcount
