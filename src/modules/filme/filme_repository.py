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

    def obter_por_id(self, filme_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT id, titulo, genero, diretor, elenco, duracao_minutos, classificacao
                FROM filmes
                WHERE id = ?
                """,
                (filme_id,),
            ).fetchone()
        return dict(row) if row else None

    def criar(self, titulo, genero, diretor, elenco, duracao_minutos, classificacao):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO filmes
                    (titulo, genero, diretor, elenco, duracao_minutos, classificacao)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (titulo, genero, diretor, elenco, duracao_minutos, classificacao),
            )
            connection.commit()
            return self.obter_por_id(cursor.lastrowid)

    def atualizar(
        self,
        filme_id,
        titulo,
        genero,
        diretor,
        elenco,
        duracao_minutos,
        classificacao,
    ):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                UPDATE filmes
                SET titulo = ?,
                    genero = ?,
                    diretor = ?,
                    elenco = ?,
                    duracao_minutos = ?,
                    classificacao = ?
                WHERE id = ?
                """,
                (
                    titulo,
                    genero,
                    diretor,
                    elenco,
                    duracao_minutos,
                    classificacao,
                    filme_id,
                ),
            )
            connection.commit()
            return cursor.rowcount

    def excluir(self, filme_id):
        with get_connection() as connection:
            cursor = connection.execute(
                """
                DELETE FROM filmes
                WHERE id = ?
                """,
                (filme_id,),
            )
            connection.commit()
            return cursor.rowcount

    def possui_sessoes(self, filme_id):
        with get_connection() as connection:
            row = connection.execute(
                """
                SELECT COUNT(*) AS total
                FROM sessoes
                WHERE filme_id = ?
                """,
                (filme_id,),
            ).fetchone()
        return row["total"] > 0
