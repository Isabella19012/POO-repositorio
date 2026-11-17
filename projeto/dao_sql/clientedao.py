from dao_sql.dao import DAO
from models.cliente import Cliente

class ClienteDAO(DAO):
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        sql = """
            INSERT INTO Cliente (nome, email, senha, fone, id_convenio)
            VALUES (?, ?, ?, ?, ?)
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(), obj.get_senha(), obj.get_fone(),  obj.get_id_convenio()))
        cls.fechar()


    @classmethod
    def listar(cls):
        cls.abrir()
        sql = "SELECT * FROM Cliente"
        cursor = cls.execute(sql)
        rows = cursor.fetchall()
        objs = [Cliente(id, nome, email, senha, fone, id_convenio) for (id, nome, email, senha, fone, id_convenio) in rows]
        cls.fechar()
        return objs

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        sql = "SELECT * FROM Cliente WHERE id = ?"
        cursor = cls.execute(sql, (id,))
        row = cursor.fetchone()
        obj = Cliente(*row) if row else None
        cls.fechar()
        return obj

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        sql = """
            UPDATE Cliente SET nome=?, email=?, senha=?, fone=?, id_convenio=?
            WHERE id=?
        """
        cls.execute(sql, (obj.get_nome(), obj.get_email(),obj.get_senha(), obj.get_fone(),  obj.get_id_convenio(), obj.get_id()))
        cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        sql = "DELETE FROM Cliente WHERE id=?"
        cls.execute(sql, (obj,))
        cls.fechar()