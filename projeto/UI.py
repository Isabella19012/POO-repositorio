from Service import Service
class UI:
    @staticmethod
    def main():
        op=-1
        while op !=0:
            op = UI.menu()
            if op == 1: UI.inserir_cliente()
            if op == 2: UI.listar_cliente()
            if op == 3: UI.listar_id_cliente()
            if op == 4: UI.listar_nome_cliente()
            if op == 5: UI.atualizar_cliente()
            if op == 6: UI.excluir_cliente()
            if op == 7: UI.inserir_servico()
            if op == 8: UI.listar_servico()
            if op == 9: UI.listar_id_servico()
            if op == 10: UI.listar_servico_descricao()
            if op == 11: UI.atualizar_servico()
            if op == 12: UI.excluir_servico()

    @staticmethod
    def menu():
        print("1-Inserir cliente, 2-Listar clientes, 3-Listar cliente por ID, 4-Pesquisar cliente por nome")
        print("5-Atualizar cliente, 6-Excluir cliente, 7-Inserir serviço, 8-Listar serviços")
        print("9-Listar serviço por ID, 10-Pesquisar serviço por descrição, 11-Atualizar serviço, 12-Excluir serviço, 0-Fim")
        return int(input('Informe uma opção: '))
    @staticmethod
    def inserir_cliente():
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_inserir(nome, email, fone)
    @staticmethod
    def listar_cliente():
        for obj in Service.cliente_listar(): print(obj)
    @staticmethod
    def listar_id_cliente():
        id = int(input("Informe o ID: "))
        obj = Service.cliente_listar_id(id)
        print(obj)
    @staticmethod
    def listar_nome_cliente():
        nome = input("Digite as iniciais do nome: ")
        for obj in Service.cliente_listar_nome(nome):
            print(obj)
    @staticmethod
    def atualizar_cliente():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)
    @staticmethod
    def excluir_cliente():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input('Informe o id do cliente a ser excluído: '))
        Service.cliente_excluir(id)

#separar
    @staticmethod
    def inserir_servico():
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_inserir(descricao, valor)
    @staticmethod
    def listar_servico():
        for obj in Service.servico_listar(): print(obj)
    @staticmethod
    def listar_id_servico():
        id = int(input("Informe o ID: "))
        obj = Service.servico_listar_id(id)
        print(obj)

    @staticmethod
    def listar_servico_descricao():
        descricao = input("Informe a descrição: ")
        for obj in Service.servico_listar_descricao(descricao):
            print(obj)
    @staticmethod
    def atualizar_servico():
        for obj in Service.servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser atualizado: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_atualizar(id, descricao, valor)

    @staticmethod
    def excluir_servico():
        for obj in Service.servico_listar(): print(obj)
        id = int(input('Informe o id do serviço a ser excluído: '))
        Service.servico_excluir(id)

UI.main()