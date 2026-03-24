class Triangulo:
    def __init__(self):
        self.b = 0  #dados de uma varievel dessa class
        self.h = 0
    def calc_area(self):    #métado
         return self.b * self.h / 2

x = Triangulo() #chama o metado __init__(ele traz uma variavel na linguagem do computador e quanda as informações)
print(x.b, x.h)
x.b = float(input('informe a base do triângulo\n'))
x.h = float(input('informe a altura do triângulo\n'))
print(x.b, x.h)
a = x.calc_area()
print(f'Aréa do triangulo é: {a:.2f}')

y = Triangulo()
print(y.b, y.h)
y.b = float(input('informe a base do segundo triângulo\n'))
y.h = float(input('informe a altura do segundo triângulo\n'))
print(y.b, y.h)
a = y.calc_area()
print(f'Aréa do triangulo é: {a:.2f}')