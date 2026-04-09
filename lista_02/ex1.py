class Agua:
    def __init__(self):
        self.mes=0
        self.consumo=0
        self.ano = 0
    def calc_agua(self):
        self.consumo = self.mes/self.ano
        return self.consumo
    def em_(self):
        self.consumo_m3=self.consumo/1000
        return self.consumo_m3
a=Agua
a.mes=input('Mês: ')
#if a.mes == 'Janeiro' or 'Fevereiro' or 'Março' or 'Abril' or 'Maio' or 'Junho'or 'Julho' or 'Agosto' or 'Setembro' or 'Outubro' or 'Novembro' or 'Dezembro':
a.ano = int(input('ano:'))
a.consumo=int(input('Consumo em m3:'))
taxa = 38,00
if 11 >= a.consumo:
    taxa = taxa + (5,00*a.consumo)
    if a.consumo >= 21:
        taxa= taxa +(6,00*a.consumo)

else: print('esse mês não existe')
print('valor a ser pago:', taxa)
