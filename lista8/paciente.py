from datetime import datetime 
from datetime import date

class paciente:
    def __init__(self, nome, cpf, fone, dt_nasc):
        self.__nome=nome
        self.__cpf=cpf
        self.__fone = fone
        self.__dt_nasc = dt_nasc
    def __str__(self):
        return f'{self.__nome} - {self.__cpf} - {self.__fone} - {self.__dt_nasc.strftime('d%/m%/Y%')}'
    def idade(self):
        p=datetime.now() - self.__dt_nasc
        dias = p.days
        anos = dias//365
        meses = dias % 365 //30
        return f'{anos} anos e {meses} mes(es)'