class AtendimentoItens:
    def __init__(self, id, id_atendimento, id_servico, quantidade, valor):
        self.set_id(id)
        self.set_id_atendimento(id_atendimento)
        self.set_id_servico(id_servico)
        self.set_quantidade(quantidade)
        self.set_valor(valor)
    def __str__(self):
        return f' {self.__id} - {self.__id_atendimento} - {self.__id_servico} - {self.__quantidade} - {self.__valor}'
    def set_id(self, id):
        if id < 0: raise ValueError("ID deve ser positivo")
        self.__id = id
    def set_quantidade(self, qtd):
        if qtd < 0: raise ValueError("Deve ser maior que 0")
        self.__quantidade = qtd
    def set_id_servico(self, id):
        if id < 0: raise ValueError("ID do serviço deve ser positivo")
        self.__id_servico = id
    def set_id_atendimento(self, id):
        if id < 0: raise ValueError("ID deve ser positivo")
        self.__id_atendimento = id
    def set_valor(self, s):
        if s < 0: raise ValueError("Valor deve ser maior que 0")
        self.__valor= s

    def get_id(self) : return self.__id
    def get_valor(self) : return self.__valor
    def get_quantidade(self) : return self.__quantidade
    def get_id_atendimento(self) : return self.__id_atendimento
    def get_id_servico(self): return self.__id_servico
    def to_json(self):
        return {'id': self.__id, 'id_atendimento': self.__id_atendimento, 'id_servico': self.__id_servico,'quantidade': self.__quantidade, 'valor': self.__valor}
    @staticmethod
    def from_json(dic):
        c = AtendimentoItens(dic['id'], dic['id_atendimento'],dic['id_servico'], dic['quantidade'], dic['valor'])
        return c