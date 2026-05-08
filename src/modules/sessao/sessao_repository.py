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

    def obter_por_id(self, sessao_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT
                    s.id,
                    s.cinema_id,
                    s.filme_id,
                    s.sala,
                    s.inicio,
                    s.intervalo_minutos,
                    c.nome AS cinema,
                    f.titulo AS filme
                FROM sessoes s
                JOIN cinemas c ON c.id = s.cinema_id
                JOIN filmes f ON f.id = s.filme_id
                WHERE s.id = ?
                """,
                (sessao_id,),
            ).fetchone()
        return dict(row) if row else None

    def criar(self, cinema_id, filme_id, sala, inicio, intervalo_minutos):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO sessoes
                    (cinema_id, filme_id, sala, inicio, intervalo_minutos)
                VALUES (?, ?, ?, ?, ?)
                """,
                (cinema_id, filme_id, sala, inicio, intervalo_minutos),
            )
            connection.commit()
            return self.obter_por_id(cursor.lastrowid)

    def atualizar(self, sessao_id, cinema_id, filme_id, sala, inicio, intervalo_minutos):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                UPDATE sessoes
                SET cinema_id = ?,
                    filme_id = ?,
                    sala = ?,
                    inicio = ?,
                    intervalo_minutos = ?
                WHERE id = ?
                """,
                (cinema_id, filme_id, sala, inicio, intervalo_minutos, sessao_id),
            )
            connection.commit()
            return cursor.rowcount

    def excluir(self, sessao_id):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                DELETE FROM sessoes
                WHERE id = ?
                """,
                (sessao_id,),
            )
            connection.commit()
            return cursor.rowcount

    def cinema_existe(self, cinema_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT COUNT(*) AS total
                FROM cinemas
                WHERE id = ?
                """,
                (cinema_id,),
            ).fetchone()
        return row["total"] > 0

    def filme_existe(self, filme_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT COUNT(*) AS total
                FROM filmes
                WHERE id = ?
                """,
                (filme_id,),
            ).fetchone()
        return row["total"] > 0

    def obter_capacidade_cinema(self, cinema_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT capacidade
                FROM cinemas
                WHERE id = ?
                """,
                (cinema_id,),
            ).fetchone()
        return row["capacidade"] if row else None

    def obter_total_publico(self, sessao_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT COALESCE(SUM(quantidade), 0) AS total
                FROM publicos
                WHERE sessao_id = ?
                """,
                (sessao_id,),
            ).fetchone()
        return row["total"]

    def existe_conflito(self, cinema_id, sala, inicio, ignorar_sessao_id=None):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT COUNT(*) AS total
                FROM sessoes
                WHERE cinema_id = ?
                  AND sala = ?
                  AND inicio = ?
                  AND (? IS NULL OR id <> ?)
                """,
                (cinema_id, sala, inicio, ignorar_sessao_id, ignorar_sessao_id),
            ).fetchone()
        return row["total"] > 0

    def possui_publico(self, sessao_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT COUNT(*) AS total
                FROM publicos
                WHERE sessao_id = ?
                """,
                (sessao_id,),
            ).fetchone()
        return row["total"] > 0
