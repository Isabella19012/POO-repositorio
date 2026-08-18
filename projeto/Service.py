from models.Servico import Servico
from models.ServicoDAO import ServicoDAO
from models.Cliente import Cliente
from models.ClienteDAO import ClienteDAO
from models.Profissional import Profissional
from models.ProfissionalDAO import ProfissionalDAO
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
    def cliente_inserir(nome, email, fone, senha, nascimento):
        obj = Cliente(0, nome, email, fone, senha, nascimento)
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
    def cliente_atualizar(id, nome, email, fone, senha, nascimento):
        obj = Cliente(id, nome, email, fone, senha, nascimento)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    @staticmethod
    def profissional_inserir(nome, email, especializacao, senha):
        obj=Profissional(0, nome, email, especializacao, senha)
        ProfissionalDAO().inserir(obj)
    @staticmethod
    def profissional_listar():
        return ProfissionalDAO().listar()
    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)
    @staticmethod
    def profissional_listar_nome(nome):
        return ProfissionalDAO().listar_nome(nome)
    @staticmethod
    def profissional_atualizar(id, nome, email, especializacao, senha):
        obj=Profissional(id, nome, email, especializacao, senha)
        ProfissionalDAO().atualizar(obj)
    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO().excluir(id)