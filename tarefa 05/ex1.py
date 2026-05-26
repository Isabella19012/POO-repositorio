from datetime import datetime
class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)
    def set_id(self,id):
        if id<0: raise ValueError('Não pode ser menor que 0.')
        self.__id=id
    def set_data(self, d):
        if d == "": raise ValueError('Não pode estar vazia.')
        self.__data=d
    def set_distancia(self, d):
        if d <0: raise ValueError('Não pode ser menor que 0')
        self.__distancia=d
    def set_tempo(self, t):
        self.__tempo=t
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_distancia(self): return self.__distancia
    def get_tempo(self): return self.__tempo
    def __str__(self):
        return f'ID: {self.__id} | Data: {self.__data} | distância: {self.__distancia} | Tempo: {self.__tempo}'
class TreinoUI:
    __treinam=[]
    @staticmethod
    def main():
        op=0
        while op != 7:
            op=TreinoUI.menu()
            if op == 1: TreinoUI.inserir()
            if op == 2: TreinoUI.listar()
            if op == 3: TreinoUI.listar_id()
            if op == 4: TreinoUI.atualizar()
            if op == 5: TreinoUI.excluir()
            if op == 6: TreinoUI.maisrapido()
    @staticmethod
    def menu():
        print("1-Inserir | 2-listar | 3-Listar ID | 4-atualizar | 5-Excluir | 6-Maior tempo | 7-Fim.")
        return int(input('Escolha uma das opções: '))
    @classmethod
    def inserir(cls):
        id=int(input('Informe o ID: '))
        data=datetime.strptime(input('Informe a data: '),('%d/%m/%Y'))
        distancia=float(input('Informe a distância: '))
        tempo = datetime.timedelta(minute=data)-distancia #como assim
        t=Treino(id, data, distancia, tempo)
        cls.__treinam.append(t)
    @classmethod
    def listar(cls):
        for t in cls.__treinam:
            print(t)
    @classmethod
    def listar_id(cls):
        id=int(input('Informe o ID: '))
        for t in cls.__treinam:
            if t.get_id()==id:
                print(t)
    @classmethod
    def atualizar(cls):
        id=int(input('Informe o ID: '))
        for t in cls.__treinam:
            if t.get_id()==id:
                data=datetime.strptime(input('Informe a data: '),('%d/%m/%Y'))
                distancia=float(input('Informe a distância: '))
                tempo=datetime.now()-data
                t.set_data(data)
                t.set_distancia(distancia)
                t.set_tempo(tempo)
    @classmethod
    def excluir(cls):
        id=int(input('Informe o ID: '))
        for t in cls.__treinam:
            if t.get_id()==id:
                cls.__treinam.remove(t)
    @classmethod
    def maisrapido(cls):
        tm=0
        for x in cls.__treinam:
            tm = tm + x.get_tempo()
        print(f'velocidade média: {tm/len(cls.__treinam)}')
TreinoUI.main()