
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
from models.Convenio import Convenio
from models.ConvenioDAO import ConvenioDAO
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
    def cliente_inserir(id, nome, email, senha,fone, id_convenio):
        c = Cliente(id, nome, email, senha, fone)
        c.set_id_convenio=(id_convenio)
        ClienteDAO().inserir(c)
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
    def cliente_atualizar(id, nome, email, fone, senha, id_convenio):
        obj = Cliente(id, nome, email, fone, senha, id_convenio)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin": return 
        Service.cliente_inserir("admin", "admin", "1234", "fone")
    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}

            return None
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
#CONVENIO
    @staticmethod
    def convenio_inserir(nome, contato, fone):
        obj = Convenio(0, nome, contato, fone)
        ConvenioDAO().inserir(obj)
    @staticmethod
    def convenio_listar():
        return ConvenioDAO().listar()
    @staticmethod
    def convenio_atualizar(id, nome, contato, fone):
        obj = Convenio(id, nome, contato, fone)
        ConvenioDAO().atualizar(obj)
    @staticmethod
    def convenio_excluir(id):
        ConvenioDAO().excluir(id)