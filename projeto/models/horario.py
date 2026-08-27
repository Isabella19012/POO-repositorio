from datetime import datetime
class Horario:
    def __init__(self, id, data):
        self.set_id(id)
        self.set_date(data)
        self.set_confirmado(False)
        self.set_id_cliente(0)
        self.set_id_servico(0)
    def __str__(self):
        return f'{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}'
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico

    def set_id(self, id):
        self.__id=id
    def set_data(self, dt):
        self.__id=dt
    def set_confirmado(self, conf):
        self.__confirmado=conf
    def set_id_cliente(self, id):
        self.__id=id
    def set_id_servico(self, id):
        self.__id=id
    def to_json(self):
        dic = {"id":self.__id, "data" :self.__data, 'confirmado':self.__confirmado, 'id_cliente':self.__id_cliente, 'id_servico': self.__id_servico}
        return dic
    @staticmethod
    def from_json(dic):
        horario = Horario(dic["id"], datetime.strftime('%d/%m/%Y %H:%M'))
        horario.set_confirmado(dic['confirmado'])
        horario.set_id_cliente(dic['id_cliente'])
        horario.set_id_servico(dic['id_servico'])
        return horario
        