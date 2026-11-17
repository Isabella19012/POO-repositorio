from dao_sql.dao import DAO
from models.horario import Horario

class horarioDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO Horario (data, confirmado, id_cliente ,id_servico, id_profissional)
            VALUES (?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_data(), obj.get_confirmado(), obj.get_id_cliente(), obj.get_id_servico, obj.get_id_profissional()))
        cls.fechar()


    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM Horario"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Horario(id, data, confirmado, id_cliente ,id_servico) for (id, data, confirmado, id_cliente ,id_servico) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM Horario WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Horario(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE Horario SET data=?, confirmado=?, id_cliente=?, id_servico=?, id_profissional=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_data(), obj.get_confirmado(), obj.get_id_cliente(), obj.get_id_servico(), obj.get_id_profissional, obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM Horario WHERE id=?"
        cls.execute(sql, (obj,))
        cls.fechar()