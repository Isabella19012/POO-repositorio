class Contato:
    def __init__(self, id, nome, email, telefone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(telefone)
    def set_id(self, id):
        if id < 0: raise ValueError('menor que 0')
        self.__id = id
    def set_nome(self, nome):
        if nome == '': raise ValueError ('nome deve ser string')
        self.__nome = nome
    def set_email(self, email):
        if email == '': raise ValueError ('email deve ser string')
        self.__email = email
    def set_fone(self, fone):
        self.__telefone = fone
    def get_nome(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__telefone
    def __str__(self):
        return f'{self.__id} - {self.__nome} - {self.__email} - {self.__telefone}'
class ContatoUI:
    contatos = []
    @staticmethod
    def main():
        op = 0
        while op != 6: 
            op = ContatoUI.menu()
            if op ==1: ContatoUI.Inserir()
            if op ==2: ContatoUI.listar()
            if op==3: ContatoUI.atualizar()
    @staticmethod
    def menu():
        print('1-Inserir 2-Listar 3-Atualizar 4-Excluir 5-Pesquisar 6-Fim')
        return int(input('Escolha uma opção: '))
    @classmethod
    def Inserir(cls):
        id = int(input('Seu id: '))
        nome = input('Seu nome: ')
        email = input('Seu email: ')
        telefone = input('Seu telefone: ')
        x=Contato(id, nome, email, telefone)
        cls.contatos.append(x)
        print('Contato inserido com sucesso')
    @classmethod
    def listar(cls):
        if len (cls.contatos) == 0: print('Nenhum contato')
        else:
            for x in cls.contatos: print(x)
    @classmethod
    def atualizar(cls, nome, email, telefone):
        o = int(input('Você quer atualizar o quê? (1-id 2-nome 3-email 4-telefone 5-nada)'))
        while o != 6:
            if o == 1:
                id=int(input('Digite seu novo id: '))
                x=Contato(id, nome, email, telefone)
                cls.contatos.append(x)            

ContatoUI.main()