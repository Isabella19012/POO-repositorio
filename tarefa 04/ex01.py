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
    times=[]
    jogador=[]
    @staticmethod
    def main():
        op = 0
        while op != 11: 
            op = UI.menu()
            if op ==1: UI.inserir_time()
            if op ==2: UI.listar_time()
            if op==3: UI.atualizar_time()
            if op==4:UI.excluir_time()
            if op ==5: UI.inserir_jogador()
            if op ==6: UI.listar_jogador()
            if op==7: UI.atualizar_jogador()
            if op==8:UI.excluir_jogador()
            if op==9:UI.listar_jogadores_do_time()
            if op==10:UI.tranferir_jogador()
    @staticmethod
    def menu():
        print('-------------------------------------------------------------------')
        print('1-Inserir time, 2-Listar time, 3-atualizar time, 4-excluir time')
        print('5-Inserir jogador, 6-Listar jogador, 7-atualizar jogador')
        print('8-excluir jogador, 9-Listar jogadores do time, 10-Transferir jogadores, 11-Fim')
        print('-------------------------------------------------------------------')
        return int(input('Escolha uma opção: '))
    @classmethod
    def inserir_time(tim):
        id=(int(input("id do time: ")))
        nome=(input('Nome do time: '))
        estado_fed=(input("Insira o estado do time: "))
        t=Times(id, nome, estado_fed)
        tim.times.append(t)
        print('Time cadastrado com sucesso')
    @classmethod
    def listar_time(tim):
        if len(tim.times) !=0:
            for x in tim.times:
                print(x)
        else: print('Não há times registrados.')
    @classmethod
    def atualizar_time(tim):
        if len(tim.times) == 0:
            print('Nenhum time')
            return

        for i, c in enumerate(tim.times):
            print(f'{i} -> {c}')

        i = int(input('Digite o índice do time: '))
        if i < 0 or i >= len(tim.times):
            print('Índice inválido')
            return

        c = tim.times[i]

        print('1-id do time | 2-nome do time | 3-estado do time | 4-sair')
        o = int(input('O que deseja atualizar? '))

        if o == 1:
            novo_id = int(input('Novo id: '))
            c.set_id(novo_id)
        elif o == 2:
            nome = input('Novo nome: ')
            c.set_nome(nome)
        elif o == 3:
            estado_fed = input('Novo telefone: ')
            c.set_estado_fed(estado_fed)
        print('Atualizado com sucesso')
    @classmethod
    def excluir_time(tim):
        if len(tim.times) == 0:
            print('Nenhum time')
            return
        for i, c in enumerate(tim.times):
            print(f'{i} -> {c}')
        i = int(input('Digite o índice do time que deseja excluir: '))
        if i < 0 or i >= len(tim.times):
            print('Índice inválido')
            return
        tim.times.pop(i)
        print('Time excluído com sucesso')
    @classmethod
    def inserir_jogador(jog):
        id=(int(input('Insira o id do jogador: ')))
        idTime=(int(input("Insira o id do time: ")))
        nome=input('Nome do jogador: ')
        camisa=(int(input("Camisa do jogador: ")))
        j=Jogador(id, idTime, nome, camisa)
        jog.jogador.append(j)
        print('Dados cadastrados com sucesso')
    @classmethod
    def listar_jogador(jog):
        if len(jog.jogador) !=0:
            for jo in jog.jogador:
                print(jo)
        else: print('Não há jogadores registrados.')
    @classmethod
    def atualizar_jogador(jog):
        if len(jog.jogador) == 0:
            print('Nenhum jogador')
            return

        for i, c in enumerate(jog.jogador):
            print(f'{i} -> {c}')

        i = int(input('Digite o índice do jogador: '))
        if i < 0 or i >= len(jog.jogador):
            print('Índice inválido')
            return
        c = jog.jogador[i]

        print('1-id do jogador | 2-nome do jogador 3-id do time | 4-camisa')
        o = int(input('O que deseja atualizar? '))

        if o == 1:
            novo_id = int(input('Novo id: '))
            c.set_id(novo_id)
        elif o == 2:
            nome = input('Novo nome: ')
            c.set_nome(nome)
        elif o == 3:
            idTime = int(input('Novo id do time: '))
            c.set_idTime(idTime)
        elif o == 4:
            camisa = int(input("Nova camisa: "))
            c.set_camisa(camisa)
        print('Atualizado com sucesso')
    @classmethod
    def excluir_jogador(jog):
        if len(jog.jogador) == 0:
            print('Nenhum time')
            return
        for i, c in enumerate(jog.jogador):
            print(f'{i} -> {c}')
        i = int(input('Digite o índice do jogador que deseja excluir: '))
        if i < 0 or i >= len(jog.jogador):
            print('Índice inválido')
            return
        jog.jogador.pop(i)
        print('Jogador excluído com sucesso')
    @classmethod
    def listar_jogadores_do_time(tim):
        if len(tim.times) == 0:
            print("Não há times cadastrados")
            return

        id_time = int(input("Digite o id do time: "))
        encontrou_time = False
        for t in tim.times:
            if t.get_id() == id_time:
                encontrou_time = True
                print(f"\nTime: {t.get_nome()}\n")

                encontrou_jogador = False

                for j in tim.jogador:
                    if j.get_idTime() == id_time:
                        print(j)
                        encontrou_jogador = True

                if not encontrou_jogador:
                    print("Esse time não possui jogadores")

        if not encontrou_time:
            print("Time não encontrado")
    @classmethod
    def tranferir_jogador(cls):

        if len(cls.jogador) == 0:
            print("Não há jogadores cadastrados")
            return

        if len(cls.times) == 0:
            print("Não há times cadastrados")
            return

        print("\nJogadores cadastrados:")
        for j in cls.jogador:
            print(j)

        id_jogador = int(input("\nDigite o id do jogador que deseja transferir: "))
        jogador_encontrado = None
        for j in cls.jogador:
            if j.get_id() == id_jogador:
                jogador_encontrado = j
                break

        if jogador_encontrado is None:
            print("Jogador não encontrado")
            return

        print("\nTimes disponíveis:")
        for t in cls.times:
            print(t)
        novo_time = int(input("\nDigite o id do novo time: "))
        time_existe = False
        for t in cls.times:
            if t.get_id() == novo_time:
                time_existe = True
                break

        if not time_existe:
            print("Time não encontrado")
            return

        jogador_encontrado.set_idTime(novo_time)

        print("Jogador transferido com sucesso")
UI.main()