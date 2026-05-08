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

    def obter_por_id(self, cinema_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT id, nome, cidade, estado, endereco, capacidade
                FROM cinemas
                WHERE id = ?
                """,
                (cinema_id,),
            ).fetchone()
        return dict(row) if row else None

    def criar(self, nome, cidade, estado, endereco, capacidade):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO cinemas (nome, cidade, estado, endereco, capacidade)
                VALUES (?, ?, ?, ?, ?)
                """,
                (nome, cidade, estado, endereco, capacidade),
            )
            connection.commit()
            return self.obter_por_id(cursor.lastrowid)

    def atualizar(self, cinema_id, nome, cidade, estado, endereco, capacidade):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                UPDATE cinemas
                SET nome = ?, cidade = ?, estado = ?, endereco = ?, capacidade = ?
                WHERE id = ?
                """,
                (nome, cidade, estado, endereco, capacidade, cinema_id),
            )
            connection.commit()
            return cursor.rowcount

    def excluir(self, cinema_id):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                DELETE FROM cinemas
                WHERE id = ?
                """,
                (cinema_id,),
            )
            connection.commit()
            return cursor.rowcount

    def possui_sessoes(self, cinema_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT COUNT(*) AS total
                FROM sessoes
                WHERE cinema_id = ?
                """,
                (cinema_id,),
            ).fetchone()
        return row["total"] > 0

    def maior_publico_por_sessao(self, cinema_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT COALESCE(MAX(total_publico), 0) AS maior_total
                FROM (
                    SELECT COALESCE(SUM(p.quantidade), 0) AS total_publico
                    FROM sessoes s
                    LEFT JOIN publicos p ON p.sessao_id = s.id
                    WHERE s.cinema_id = ?
                    GROUP BY s.id
                ) totais
                """,
                (cinema_id,),
            ).fetchone()
        return row["maior_total"]
