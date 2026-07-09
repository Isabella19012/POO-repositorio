class Viagem:
    def __init__(self):
        self.__destino= ''
        self.__distancia=0.0
        self.__litro=0.0
    def set_destino(self,d):
        self.__destino = d
    def set_distancia(self,d):
        if d >=0: self.__distancia = d
        else: raise ValueError()
    def set_litros(self,d):
        if d >0: self.__litro = d
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

class ViagemUI:
    @staticmethod
    def main():
        op = ViagemUI.menu()
        while op != 2:
            if op == 1:
                ViagemUI.calculo()
            op = ViagemUI.menu()

    @staticmethod
    def menu():
        print("1 - Calcular, 2 - Fim")
        op = int(input("Informe uma opção: "))
        return op
    @staticmethod
    def calculo():
        v=Viagem()
        v.set_destino(input("Informe o destino: "))
        v.set_distancia(float(input('Informe a distancia em km: ')))
        v.set_litros(float(input('Informe a quantidade de litros gastos:')))
        print(v)
        print(f'Seu consumo médio foi de {v.consumo_m()}')
ViagemUI.main()