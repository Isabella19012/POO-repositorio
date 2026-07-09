from models.Servico import Servico
from models.ServicoDAO import ServicoDAO
from models.Cliente import Cliente
from models.ClienteDAO import ClienteDAO
class Service:
    # Serviços
    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_listar_descricao(descricao):
        return ServicoDAO().listar_descricao(descricao)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)
    # Clientes
    @staticmethod
    def cliente_inserir(nome, email, fone):
        obj = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_listar_nome(nome):
        return ClienteDAO().listar_nome(nome)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)