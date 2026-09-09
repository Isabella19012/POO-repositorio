from datetime import datetime
class Atendimento:
    def __init__(self, id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        self.set_id(id)
        self.set_data(data)
        self.set_queixa_principal(queixa_principal)
        self.set_historico_saude(historico_saude)
        self.set_avaliacao(avaliacao)
        self.set_prescricao(prescricao)
        self.set_id_horario(id_horario)
    def __str__(self):
        return f'{self.__id} - {self.__data} - {self.__queixa_principal} - {self.__historico_saude} - {self.__avaliacao} - {self.__prescrisao} - {self.__id_horario}'
    def set_id(self, id):
        if id<0: raise ValueError('O id não pode ser negativo')
        self.__id = id
    def set_data(self, dt):
        if dt > datetime.now(): raise ValueError('Não pode estar no futuro')
        self.__data = dt
    def set_queixa_principal(self, qx):
        if qx == '': raise ValueError('Deve ser texto.')
        self.__queixa_principal = qx
    def set_historico_saude(self, hs):
        if hs == '': raise ValueError('Deve ser texto.')
        self.__historico_saude = hs
    def set_avaliacao(self, hs):
        if hs == '': raise ValueError('Deve ser texto.')
        self.__avaliacao = hs
    def set_prescricao(self, hs):
        if hs == '': raise ValueError('Deve ser texto.')
        self.__prescrisao = hs
    def set_id_horario(self, id):
        if id<=0: raise ValueError('O id não pode ser negativo')
        self.__id_horario = id
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_queixa_principal(self): return self.__queixa_principal
    def get_historico_saude(self): return self.__historico_saude
    def get_avaliacao(self): return self.__avaliacao
    def get_prescricao(self):return self.__prescrisao
    def get_id_horario(self): return self.__id_horario
    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "queixa_principal": self.__queixa_principal,
            "historico_saude": self.__historico_saude,
            "avaliacao": self.__avaliacao,
            "prescricao": self.__prescrisao,
            "id_horario": self.__id_horario
        }

    @staticmethod
    def from_json(dic):
        return Atendimento(
            dic["id"],
            datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"),
            dic["queixa_principal"],
            dic["historico_saude"],
            dic["avaliacao"],
            dic["prescricao"],
            dic["id_horario"]
        )