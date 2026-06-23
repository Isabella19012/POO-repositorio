import json
class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
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
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
    def to_json(self):
        return {'id': self.__id, 'nome': self.__nome, 'email': self.__email,  'fone': self.__fone}
    @staticmethod
    def from_json(dic):
        return Cliente(dic['id'], dic['nome'], dic['email'], dic['fone'])
class ClienteUI:
    __cliente=[]
    @staticmethod
    def main():
        ClienteUI.abrir()
        op = 0
        while op != 9:
            op = ClienteUI.menu()
            if op == 1: ClienteUI.inserir()
            if op == 2: ClienteUI.listar()
            if op == 3: ClienteUI.listar_id()
            if op == 4: ClienteUI.atualizar()
            if op == 5: ClienteUI.excluir()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Listar id, 4-Atualizar, 5-Excluir, 0-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o telefone: ")
        x = ClienteUI(id, nome, email, fone)
        cls.__clientes.append(x)

    @classmethod
    def listar(cls):                
        for x in cls.__cliente: 
            print(x)
    @classmethod
    def listar_id(cls):                
        for x in cls.__cliente: 
            print(x.get_id)

    @classmethod
    def atualizar(cls):
        for x in cls.__cliente: print(x)
        id = int(input("Informe o id do objeto a ser atualizado: "))
        for x in cls.__cliente:
            if x.get_id() == id:
                nome = input("Informe o novo nome: ")
                email = input("Informe o novo email: ")
                fone = input("Informe o novo telefone: ")
                x.set_nome(nome)
                x.set_email(email)
                x.set_telefone(fone)
                ClienteUI.salvar()

    @classmethod
    def excluir(cls):
        for x in cls.__cliente: print(x)
        id = int(input("Informe o id do objeto a ser excluído: "))
        for x in cls.__cliente:
            if x.get_id() == id:
                cls.__cliente.remove(x)
                ClienteUI.salvar()
    @classmethod
    def salvar(cls):    
        arquivo = open("clientes.json", mode = "w")
        json.dump(cls.__cliente, arquivo, default = Cliente.to_json, indent = 2)
        arquivo.close()
    @classmethod
    def abrir(cls):
        try:
            arquivo = open("clientes.json", mode = "r")
            list_dic=json.load(arquivo)
            arquivo.close()
            cls.__clientes=[]
            for dic in list_dic:
                x = Cliente.from_json(dic)
                cls.__clientes.append(x)
        except FileNotFoundError:
            pass

ClienteUI.main()
ClienteUI.abrir()