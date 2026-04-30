class Pais:
    def __init__(self, nome, populacao, area):
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)

    def set_nome(self, n):
        if isinstance(n, str): self.__nome = n
        else: raise ValueError("Tem que ser string.")
    def set_populacao(self, n):
        if n >= 0: self.__populacao = n
        else: raise ValueError()
    def set_area(self, n):
        if n > 0: self.__area = n
        else: raise ValueError()
    def get_nome(self):
        return self.__nome
    def get_populacao(self):
        return self.__populacao
    def get_area(self):
        return self.__area
    def densidade(self):
        return self.__populacao/self.__area
    def __str__(self):
        return f"Nome do pais é {self.__nome}, com população de {self.__populacao} habitantes, área de {self.__area} km2 e com densidade de {self.densidade():.2f}"
        
class PaisUI:
    @staticmethod
    def menu():
        print("1 - Calcular, 2 - Fim")
        op = int(input("Informe uma opção: "))
        return op
    @staticmethod
    def main():
        op = PaisUI.menu()
        while op !=2:
            if op == 1: PaisUI.calculo()
            op = PaisUI.menu()
    @staticmethod
    def calculo():
        nome = input('Nome do país: ')
        populacao = int(input('Número de habitantes: '))
        area = float(input("Sua área: "))
        print('---------------')
        p=Pais(nome, populacao, area)
        print(p)
        print('---------------')
        print(f"Densidade de {p.densidade():.2f} por km2")

PaisUI.main()