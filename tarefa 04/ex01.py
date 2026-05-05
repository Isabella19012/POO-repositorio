class Times:
    def __init__(self, id, nome, estado_fed):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado_fed(estado_fed)

    def set_id(self,id):
        if id < 0 or isinstance(id, str): raise ValueError('não pode ser string ou ser negativo')
        else: self.__id = id 
    def set_nome(self, nome):
        if isinstance(nome, str): self.__nome = nome
        else: raise ValueError('nome não pode ser número')
    def set_estado_fed(self, estado_fed):
        if isinstance(estado_fed, str): self.__estado_fed = estado_fed
        else: raise ValueError('nome não pode ser número')
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_estado_fed(self): return self.__estado_fed
    def __str__(self): return f" id: {self.__id} - nome: {self.__nome} - estado da federação: {self.__estado_fed}. "
class Jogador:
    def __init__(self, id, idTime, nome, camisa):
        self.set_id(id)
        self.set_idTime(idTime)
        self.set_nome(nome)
        self.set_camisa(camisa)

    def set_id(self,id):
        if id < 0 or isinstance(id, str): raise ValueError('não pode ser string ou ser negativo')
        else: self.__id = id 
    def set_nome(self, nome):
        if isinstance(nome, str): self.__nome = nome
        else: raise ValueError('nome não pode ser número')
    def set_idTime(self, idT):
        if isinstance(idT, str): raise ValueError('id não pode ser string')
        else: self.__idTime = idT
    def set_camisa(self,c):
        if c < 0: raise ValueError("deve ser positivo")
        else: self.__camisa=c
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_idTime(self): return self.__idTime
    def get_camisa(self): return self.__camisa
    def __str__(self): return f" id: {self.__id} - nome: {self.__nome} - id do time: {self.__idTime} - camisa: {self.__camisa}. "

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 13: 
            op = UI.menu()
            if op ==1: UI.Inserir_time()
            if op ==2: UI.listar_time()
            if op==3: UI.atualizar_time()
            if op==4:UI.excluir_time()
            if op==5:UI.pesquisar_time()
            if op ==6: UI.Inserir_jogador()
            if op ==7: UI.listar_jogador()
            if op==8: UI.atualizar_jogador()
            if op==9:UI.excluir_jogador()
            if op==10:UI.pesquisar_jogador()
            if op==11:UI.Listar_jogadores_do_time()
            if op==11:UI.Tranferir_jogador()
    @staticmethod
    def menu():
        print('1-Inserir time, 2-Listar time, 3-atualizar time, 4-excluir time, 5-pesquisar time')
        print('6-Inserir jogador, 7-Listar jogador, 8-atualizar jogador, 9-excluir jogador, 10-persquisar jogador')
        print('11-Listar jogadores do time, 12-Transferir jogadores, 13-Fim')
        return int(input('Escolha uma opção: '))
    @staticmethod
UI.main()