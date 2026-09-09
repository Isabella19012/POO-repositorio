
from models.Servico import Servico
from models.ServicoDAO import ServicoDAO
from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.Profissional import Profissional
from models.ProfissionalDAO import ProfissionalDAO
from models.horario import Horario
from models.horariodao import horarioDAO
from models.Atendimento import Atendimento
from models.AtendimentoDAO import AtendimentoDAO
class Service:
# SERVIÇOS
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
# CLIENTES
    @staticmethod
    def cliente_inserir(nome, email, senha, fone):
        obj = Cliente(0, nome, email, senha, fone)
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
    def cliente_atualizar(id, nome, email, senha, fone):
        obj = Cliente(id, nome, email, senha, fone)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    @staticmethod
#PROFISSIONAL
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
    @staticmethod
#HORARIO
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c= Horario(0, data)
        c.set_confirmado=(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional
        horarioDAO().inserir(c) 
    @staticmethod
    def horario_listar():
        return horarioDAO().listar()
    @staticmethod
    def horario_listar_id():
        return horarioDAO().listar_id()
    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c= Horario(id, data)
        c.set_confirmado=(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        horarioDAO().atualizar(c)
    @staticmethod
    def horario_excluir(id):
        horarioDAO().excluir(id)
#ATENDIMENTO
    @staticmethod
    def atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(0, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
        AtendimentoDAO().inserir(obj)
    @staticmethod
    def atendimento_listar():
        return AtendimentoDAO().listar()
    @staticmethod
    def atendimento_atualizar(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        obj = Atendimento(id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario)
        AtendimentoDAO().atualizar(obj)
    @staticmethod
    def atendimento_excluir(id):
        AtendimentoDAO().excluir(id)