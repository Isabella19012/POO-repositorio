from datetime import datetime
import json
class Contato:
    def __init__(self, id, nome, email, fone, nasc):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_nascimento(nasc)
    def set_id(self, id):
        if id<0:raise ValueError('Id deve ser positivo')
        self.__id=id
    def set_nome(self, nome):
        if nome == '': raise ValueError('Não deve estar vazio.')
        self.__nome=nome
    def set_email(self, email):
        if email == '': raise ValueError('Não deve estar vazio.')
        self.__email=email
    def set_fone(self, fone):
        if fone == '': raise ValueError('Não deve estar vazio.')
        self.__fone=fone
    def set_nascimento(self, nasc):
        if nasc > datetime.now(): raise ValueError('nada normal')
        self.__nascimento=nasc
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_nascimento(self): return self.__nascimento

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
    def to_json(self):
        return {'id': self.__id, 'nome': self.__nome, 'email': self.__email,  'fone': self.__fone}
    @staticmethod
    def from_json(dic):
        return Contato(dic['id'], dic['nome'], dic['email'], dic['fone'])
class ContatoUI:
    __contatos=[]
    @staticmethod
    def main():
        ContatoUI.abrir()
        op = 0
        while op != 9:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.listar_id()
            if op == 4: ContatoUI.atualizar()
            if op == 5: ContatoUI.excluir()
            if op == 6: ContatoUI.pesquisar()
            if op == 7: ContatoUI.aniversariantes()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Listar id, 4-Atualizar, 5-Excluir, 6 - Pesquisar contatos, 7 - Aniversáriantes 0-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o telefone: ")
        x = Contato(id, nome, email, fone)
        cls.__contatos.append(x)

    @classmethod
    def listar(cls):                
        for x in cls.__contatos: 
            print(x)
    @classmethod
    def listar_id(cls):                
        for x in cls.__contatos: 
            print(x.get_id)

    @classmethod
    def atualizar(cls):
        for x in cls.__contatos: print(x)
        id = int(input("Informe o id do objeto a ser atualizado: "))
        for x in cls.__contatos:
            if x.get_id() == id:
                nome = input("Informe o novo nome: ")
                email = input("Informe o novo email: ")
                fone = input("Informe o novo telefone: ")
                x.set_nome(nome)
                x.set_email(email)
                x.set_telefone(fone)
                ContatoUI.salvar()

    @classmethod
    def excluir(cls):
        for x in cls.__contatos: print(x)
        id = int(input("Informe o id do objeto a ser excluído: "))
        for x in cls.__contatos:
            if x.get_id() == id:
                cls.__contatos.remove(x)
                ContatoUI.salvar()
    @classmethod
    def pesquisar(cls):
        if len(cls.__contatos) == 0:
            print('Nenhum contato')
            return
        inicio = input('Digite as iniciais do nome: ').lower()
        achou = False
        for c in cls.__contatos:
            if c.get_nome().lower().startswith(inicio):
                print(c)
                achou = True

        if not achou:
            print('Contato não encontrado')
    @classmethod
    def aniversariantes(cls):
        for x in cls.__contatos:
            if x.get_nascimento().day == datetime.now().day and x.get_nascimento().month == datetime.now().month:
                print(x, 'é aniversáriante')
    @classmethod
    def salvar(cls):    
        arquivo = open("contatos.json", mode = "w")
        json.dump(cls.__contatos, arquivo, default = Contato.to_json, indent = 2)
        arquivo.close()
    @classmethod
    def abrir(cls):
        try:
            arquivo = open("contatos.json", mode = "r")
            list_dic=json.load(arquivo)
            arquivo.close()
            cls.__contatos=[]
            for dic in list_dic:
                x = Contato.from_json(dic)
                cls.__contatos.append(x)
        except FileNotFoundError:
            pass
    

ContatoUI.main()
ContatoUI.abrir()