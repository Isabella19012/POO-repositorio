class Frete:
    def __init__(self, p, d):
        self.__peso = 0.0
        self.__distancia = 0.0
        self.set_peso(p)
        self.set_distancia(d)
    def set_peso(self,v):
        if v>=0: self.__peso = v
        else: raise ValueError()
    def set_distancia(self,v):
        if v>=0: self.__distancia = v
        else: raise ValueError()
    def get_peso(self):
        return self.__peso
    def get_distancia(self):
        return self.__distancia
    def calc_frete(self):
        return (self.__peso * self.__distancia) * 0.1
    def __str__(self):
        return f'Frete com peso: {self.__peso}, distância: {self.__distancia}'
class UI:
    @staticmethod
    def main():
        p = float(input('Digite o peso do frete: '))
        d = float(input('Digite a distância do frete: '))
        f = Frete(p, d)
        print(f'Valor do frete: {f.calc_frete():.2f}')
        print(f)
UI.main()