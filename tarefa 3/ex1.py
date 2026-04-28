class Viagem:
    def __init__(self):
        self.__destino= ''
        self.__distancia=0.0
        self.__litro=0.0
    def set_destino(self,d):
        self.__destino = d
    def set_ditancia(self,d):
        if self.__distancia >=0: self.__distancia = d
        else: raise ValueError()
    def set_litros(self,d):
        if self.__distancia >=0: self.__litro = d
        else: raise ValueError()
    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litro
    def consumo_m(self):
        return self.__distancia/self.__litro
    def __str__(self):
        return f'distancia: {self.__distancia} em KM, litros: {self.__litro} e destino: {self.__destino}'

class UI:
    @staticmethod
    def main():
        op = UI.menu()
        while op!=2:
            if op == 1: UI.calculo()
    @staticmethod
    def menu():
        print("1 - viagem, 2 - fim")
        op = int(input("Informe uma opção: "))
        return op
    @staticmethod
    def calculo():
        v=Viagem()
        v.set_destino(input("Informe o destino: "))
        v.set_ditancia(float(input('Informe a distancia em km: ')))
        v.set_litros(float(input('Informe a quantidade de litros gastos:')))
        print(f'Seu consumo médio foi de {v.consumo_m()}')
        print(Viagem())
UI.main()