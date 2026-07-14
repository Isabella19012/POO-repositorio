class Profissional:
    def __init__(self, id, nome, email, especializacao, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_especializacao(especializacao)
        self.set_senha(senha)
    def __str__(self):
        return f' {self.__id} - {self.__nome} - {self.__email} - {self.__especializacao} - {self.__senha}'
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError("E-mail deve ser informado")
        self.__email= email
    def set_especializacao(self, especializacao):
        if especializacao == "": raise ValueError("Especialidade deve ser informado")
        self.__especializacao = especializacao
    def set_senha(self, senha):
        if senha == '': raise ValueError('Senha não pode ser vazia')
        self.__senha=senha
    def get_id(self) : return self.__id
    def get_nome(self) : return self.__nome
    def get_email(self) : return self.__email
    def get_especializacao(self) : return self.__especializacao
    def get_senha(self): return self.__senha
    def to_json(self):
        return {'id': self.__id, 'nome': self.__nome, 'email': self.__email, 'especializacao': self.__especializacao, 'senha': self.__senha}
    @staticmethod
    def from_json(dic):
        return Profissional(dic['id'], dic['nome'], dic['email'], dic['especializacao'], dic['senha'])