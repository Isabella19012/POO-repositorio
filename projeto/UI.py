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
            if op == 13: UI.inserir_profissional()
            if op == 14: UI.listar_profissional()
            if op == 15: UI.listar_id_profissional()
            if op == 16: UI.listar_nome_profissional()
            if op == 17: UI.atualizar_profissional()
            if op == 18: UI.excluir_profissional()

    @staticmethod
    def menu():
        print("=" * 50)
        print("          SISTEMA DE GERENCIAMENTO")
        print("=" * 50)

        print("[ CLIENTES ]")
        print("1  - Inserir cliente")
        print("2  - Listar clientes")
        print("3  - Listar cliente por ID")
        print("4  - Pesquisar cliente por nome")
        print("5  - Atualizar cliente")
        print("6  - Excluir cliente")

        print("\n[ SERVIÇOS ]")
        print("7  - Inserir serviço")
        print("8  - Listar serviços")
        print("9  - Listar serviço por ID")
        print("10 - Pesquisar serviço por descrição")
        print("11 - Atualizar serviço")
        print("12 - Excluir serviço")

        print('\n[ PROFISSIONAL ]')
        print("13  - Inserir profissional")
        print("14  - Listar profissional")
        print("15  - Listar profissional por ID")
        print("16 - Pesquisar profissional por nome")
        print("17 - Atualizar profissional")
        print("18 - Excluir profissional")

        print("=" * 50)
        print("0-Fim")
        return int(input('Informe uma opção: '))
    @staticmethod
    def inserir_cliente(): 
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        senha = input('Informe a senha: ')
        Service.cliente_inserir(nome, email, fone, senha)
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
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        senha = input('Informe a nova senha: ')
        Service.cliente_atualizar(id, nome, email, fone, senha)
    @staticmethod
    def excluir_cliente():
        for obj in Service.cliente_listar(): print(obj)
        id = int(input('Informe o id do cliente a ser excluído: '))
        Service.cliente_excluir(id)

#separar//servico
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
    @staticmethod
    def inserir_profissional(): 
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        especializacao = input("Informe a especialização: ")
        senha = input('Informe a senha: ')
        Service.profissional_inserir(nome, email, especializacao, senha)
    @staticmethod
    def listar_profissional():
        for obj in Service.profissional_listar(): print(obj)
    @staticmethod
    def listar_id_profissional():
        id = int(input("Informe o ID: "))
        obj = Service.profissional_listar_id(id)
        print(obj)
    @staticmethod
    def listar_nome_profissional():
        nome = input("Digite as iniciais do nome: ")
        for obj in Service.profissional_listar_nome(nome):
            print(obj)
    @staticmethod
    def atualizar_profissional():
        for obj in Service.profissional_listar(): print(obj)
        id = int(input("Informe o id do profissional a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        especializacao = input("Informe a nova especializacao: ")
        senha = input('Informe a nova senha: ')
        Service.profissional_atualizar(id, nome, email, especializacao, senha)
    @staticmethod
    def excluir_profissional():
        for obj in Service.profissional_listar(): print(obj)
        id = int(input('Informe o id do profissional a ser excluído: '))
        Service.profissional_excluir(id)
UI.main()