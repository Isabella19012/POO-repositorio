from datetime import datetime
class Paciente:
    def __init__(self,id,  nome, cpf, telefone, nasc):
        self.set_id(id)
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nasc)
    def set_id(self, id):
        if id < 0: raise ValueError("O ID deve ser um número positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("O nome não pode ser vazio")
        self.__nome = nome
    def set_cpf(self, cpf):
        if cpf == "": raise ValueError("O CPF não deve ser vazio")
        self.__cpf = cpf
    def set_telefone(self, telefone):
        if telefone == "": raise ValueError("O telefone deve ser uma string")
        self.__telefone = telefone
    def set_nascimento(self, nasc):
        if nasc > datetime.now(): raise ValueError("Você nem nasceu.")
        self.__nascimento = nasc
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_cpf(self): return self.__cpf
    def get_telefone(self): return self.__telefone
    def get_nacimento(self): return self.__nascimento #ctrl +esse botão(;) da comentario mais fácil
    def idade(self):
         tempo = datetime.now() - self.__nascimento #timedelta
         anos = tempo.days//365
         meses = tempo.days %365 // 30
         return f" {anos} anos e {meses} meses"
    def __str__(self):
            return f' {self.__id} - {self.__nome} - {self.__cpf} - {self.__telefone} - {self.__nascimento.strftime('%d/%m/%Y')}'
# x = Paciente(91, "Oi", "122", '84-999999-9333', datetime(2009, 12, 3),)
# print(x)
# print(x.idade())
class PacienteUI:
    __pacientes=[]
    @staticmethod
    def main():
        op=""
        while op !=0:
            op=PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()

    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Atualizar, 4-Excluir | 5-Pesquisar 6-Aniversáriantes, 0-Fim")
        return int(input("Digite uma das opções"))
    @classmethod
    def inserir(cls):
        id=int(input('Digite o seu nome: '))
        nome=input('Digite seu nome: ')
        cpf=(input('Digite seu CPF: '))
        telefone = input("Digite seu telefone: ")
        nasc=datetime.strptime(input('Digite sua data de nascimento: '), "%d/%m/%Y")
        p = Paciente(id,  nome, cpf, telefone, nasc)
        cls.__pacientes.append(p)
    @classmethod
    def listar(cls):
        for x in cls.__pacientes:
            print(x, x.idade())
PacienteUI.main()