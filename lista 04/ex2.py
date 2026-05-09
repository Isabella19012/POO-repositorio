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
        if not isinstance(nome, str):
            raise ValueError('nome deve ser string')
        self.__nome = nome
    def set_email(self, email):
        if not isinstance(email, str):
            raise ValueError('email deve ser string')
        self.__email = email
    def set_fone(self, fone):
        if not isinstance(fone, str):
            raise ValueError('telefone deve ser string')
        self.__telefone = fone
    def get_id(self): return self.__id
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
            if op==4:ContatoUI.excluir()
            if op==5:ContatoUI.pesquisar()
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
    def atualizar(cls):
        if len(cls.contatos) == 0:
            print('Nenhum contato')
            return

        for i, c in enumerate(cls.contatos):
            print(f'{i} -> {c}')

        i = int(input('Digite o índice do contato: '))
        if i < 0 or i >= len(cls.contatos):
            print('Índice inválido')
            return

        c = cls.contatos[i]

        print('1-id 2-nome 3-email 4-telefone 5-sair')
        o = int(input('O que deseja atualizar? '))

        if o == 1:
            novo_id = int(input('Novo id: '))
            c.set_id(novo_id)
        elif o == 2:
            nome = input('Novo nome: ')
            c.set_nome(nome)
        elif o == 3:
            email = input('Novo email: ')
            c.set_email(email)
        elif o == 4:
            fone = input('Novo telefone: ')
            c.set_fone(fone)
        print('Atualizado com sucesso')
    @classmethod
    def excluir(cls):
        if len(cls.contatos) == 0:
            print('Nenhum contato')
            return

        # mostra os contatos com índice
        for i, c in enumerate(cls.contatos):
            print(f'{i} -> {c}')

        i = int(input('Digite o índice do contato que deseja excluir: '))

        if i < 0 or i >= len(cls.contatos):
            print('Índice inválido')
            return
        cls.contatos.pop(i)

        print('Contato excluído com sucesso')
    @classmethod
    def pesquisar(cls):
        if len(cls.contatos) == 0:
            print('Nenhum contato')
            return
        inicio = input('Digite as iniciais do nome: ').lower()
        achou = False
        for c in cls.contatos:
            if c.get_nome().lower().startswith(inicio):
                print(c)
                achou = True

        if not achou:
            print('Contato não encontrado')
ContatoUI.main()