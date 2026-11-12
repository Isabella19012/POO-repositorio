from dao_sql.dao import DAO
from models.Profissional import Profissional

class ProfissionalDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO Profissional (nome, email, especializacao, senha)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_especializacao(), obj.get_senha()))
        cls.fechar()


    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM Profissional"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Profissional(id, nome, email, especializacao, senha) for (id, nome, email, especializacao, senha) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM Profissional WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Profissional(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE Profissional SET nome=?, email=?, especializacao=?, senha=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_especializacao(), obj.get_senha(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM Profissional WHERE id=?"
        cls.execute(sql, (obj,))
        cls.fechar()