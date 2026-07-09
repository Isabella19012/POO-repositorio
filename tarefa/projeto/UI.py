from Service import Service
class UI:
    @staticmethod
    def main():
        op=0
        while op !=9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.listar_id()
            if op == 4: UI.atualizar()
            if op == 5: UI.excluir()
    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3 - Listar ID, 4-Atualizar, 5-Excluir, 9-Fim")
        return int(input('Informe uma opção: '))
    @staticmethod
    def inserir():
        id = int(input("Informe o id: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_inserir(id, descricao, valor)
    @staticmethod
    def listar():
        for obj in Service.servico_listar(): print(obj)
    @staticmethod
    def listar_id():
        id = int(input("Informe o ID: "))
        obj = Service.servico_listar_id(id)
        print(obj)
    @staticmethod
    def atualizar():
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        descricao = input("Informe o novo nome: ")
        valor = float(input("Informe o novo valor: "))
        Service.servico_atualizar(id, descricao, valor )
    @staticmethod
    def excluir():
        for obj in Service().servico_listar(): print(obj)
        id = int(input('Informe o id do serviço a ser excluído: '))
        Service.servico_excluir(id)
UI.main()