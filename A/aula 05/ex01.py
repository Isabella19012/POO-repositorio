class Retângulo():
    def __init__(self, b, h):
        self.__b=0.0
        self.__h=0.0
        self.set_base(b)
        self.set_altura(h)
    def set_base(self,v):
        if v>=0:
            self.__b = v
        else:
            raise ValueError()
    def set_altura(self,v):
        if v>=0:
            self.__h = v
        else:
            raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b*self.__h
    def calc_diagonal(self):
        return (self.__b**2+self.__h**2)**0.5
    def __str__(self):
        return f'Retângulo com altura: {self.__h} e base: {self.__b}'
class UI:
    @staticmethod
    def main():
        b = float(input('Digite a base do retângulo: '))
        h = float(input('Digite a altura do retângulo: '))
        r = Retângulo(b, h)
        print(f'Área: {r.calc_area()}')
        print(f'Diagonal: {r.calc_diagonal():.2f}')

UI.main()