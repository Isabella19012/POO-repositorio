import enum
from datetime import datetime
class Grupo(enum.Enum):
    A=1
    B=2
    C=3
    D=4
    E=5
    F=6
    G=7
    H=8
    I=9
    J=10
    K=11
    L=12
class Fase(enum.Enum):
    Grupos=1
    DezesseisAvos=2
    Oitavas=3
    Quartas=4
    Seminfinais=5
    TerceiroLugar=6
    Final=7
class Pais:
    def __init__(self, id, nome, sigla, grupo):
        self.set_id(id)
        self.set_nome(nome)
        self.set_sigla(sigla)
        self.set_grupo(grupo)
    def set_id(self, id):
        if id < 0: raise ValueError('ID não pode ser negativo.')
        self.__id=id
    def set_nome(self, nome):
        if nome == '': raise ValueError('Você deve ter um nome.')
        self.__nome=nome
    def set_sigla(self, s):
        if s == '': raise ValueError('Você deve ter um nome.')
        self.__sigla=s
    def set_grupo(self, grupo):
        if 0<grupo<=12: self.__grupo = grupo
        else: raise ValueError('') #pode ser sujeito a alterações
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_sigla(self): return self.__sigla
    def get_grupo(self): return self.__grupo
    def __str__(self):
        return f'{self.__id} - {self.__nome} - {self.__sigla} - {self.__grupo}'
class Jogo:
    def __init__(self, id, id_pais1, id_pais2, gols1, gols2, fase, data_hora):
        self.set_id(id)
        self.set_id_pais1(id_pais1)
        self.set_id_pais2(id_pais2)
        self.set_gols1(gols1)
        self.set_gols2(gols2)
        self.set_fase(fase)
        self.set_data_hora(data_hora)
    def set_id(self, id):
        if id < 0: raise ValueError('ID não pode ser negativo.')
        self.__id=id
    def set_id_pais1(self, id1):
        if id1 < 0: raise ValueError('ID não pode ser negativo.')
        self.__id_pais1=id1
    def set_id_pais2(self, id2):
        if id2 < 0: raise ValueError('ID não pode ser negativo.')
        self.__id_pais2=id2
    def set_gols1(self, gol):
        if gol < 0: raise ValueError('Gol não pode ser negativo.')
        self.__gols1=gol
    def set_gols2(self, gol):
        if gol < 0: raise ValueError('Gol não pode ser negativo.')
        self.__gols2=gol
    def fase(self, fase):
        if 0<fase<=12: self.__fase = fase
        else: raise ValueError('') #pode ser sujeito a alterações
    def data_hora(self, dh):
        if dh < datetime.now(): raise ValueError('O jogo já aconteceu')
        self.__data_hora=dh
    def get_id(self): return self.__id
    def get_id_pais1(self): return self.__id_pais1
    def get_id_pais2(self): return self.__id_pais2
    def get_gols1(self): return self.__gols1
    def get_gols2(self): return self.__gols2
    def get_fase(self): return self.__fase
    def get_data_hora(self): return self.__data_hora
    def __str__(self):
        return f'{self.__id} - {self.__id_pais1} - {self.__id_pais2} - {self.__gols1} - {self.__gols1} - {self.__gols2} - {self.__fase} - {self.__data_hora}'

class UI:
    __paises=[]
    __jogos=[]
    @staticmethod
    def main():
        op=-1
        while op != 0:
            op=UI.menu()
            if op == 1: UI.cadastrar_pais()
            if op == 2: UI.cadastrar_jogo()
            if op == 3: UI.listar_pais()
            if op == 4: UI.listar_jogo()
    @staticmethod
    def menu():
        print('1 - Cadastrar pais, 2 - Cadastrar jogo, 3 - Listar pais, 4 - Listar jogo, 0 - Fim.')
        return int(input('Digite uma das opções: '))
    @classmethod
    def cadastrar_pais(cls):
        id=int(input('Insira seu ID: '))
        nome=input('Insire o nome')
        sigla=input('Insira a sigla')
        grupo=Grupo.input('Insira o grupo de A a L: ')
        x=Pais(id, nome, sigla, grupo)
        cls.__paises.append(x)
UI.main()