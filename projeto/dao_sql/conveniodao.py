from dao_sql.dao import DAO
from models.Convenio import Convenio

class ConvenioDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO Convenio (nome, contato, fone)
            VALUES (?, ?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_contato(), obj.get_fone()))
        cls.fechar()


    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM Convenio"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Convenio(id, nome, contato, fone) for (id, nome, contato, fone) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM Convenio WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Convenio(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE Convenio SET nome=?, contato=?, fone=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_nome(), obj.get_contato(), obj.get_fone(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM Convenio WHERE id=?"
        cls.execute(sql, (obj,))
        cls.fechar()