from datetime import datetime
from enum import Enum
class Pagamento (Enum):
    EmAberto=1
    PagoParcial=2
    Pago=3
class Boleto:
    def __init__(self, codbarras, dataEmissao, datavencimento, valorboleto):
        #atributos que serão validados
        self.set_codbarras(codbarras)
        self.set_dataemissao(dataEmissao)
        self.set_datavencimento(datavencimento)
        self.set_valorboleto(valorboleto)
        #atributos com valor inicial pré-definidos
        self.__data_pagto=None
        self.__valorpago=0
        self.__situacaopagamento=Pagamento.EmAberto
    def set_codbarras(self,c):
        if len(c) ==10: self.__cod=c
        else: raise ValueError('Código deve ter 10 digitos')
    def set_dataemissao(self,dt_emissao):
        if dt_emissao > datetime.now(): raise ValueError('Data não pode ser no futuro.')
        self.__dataemissao=dt_emissao
    def set_datavencimento(self,venc):
        if venc < datetime.now(): raise ValueError('Não se cria boleto vencido.')
        self.__datavenc=venc
    def set_valorboleto(self, v_boleto):
        if v_boleto<0: raise ValueError('Boleto não pode ser 0')
        self.__valorboleto=v_boleto
    #substituiu: set_valor_pago, set_data_pagamento e set_situacao_pagamento
    def pagar(self, valor_pago):
        if valor_pago <0: raise ValueError("Valor pago não pode ter valor negativo")
        if self.__situacaopagamento != Pagamento.EmAberto: raise ValueError('Boleto á pago')
        self.__valorpago=valor_pago
        self.__data_pagto=datetime.now()
        if self.__valorboleto == self.__valorpago: self.__situacaopagamento=Pagamento.Pago
        else: self.__situacaopagamento=Pagamento.PagoParcial
    def get_codbarras(self): return self.__cod
    def get_dataemissao(self): return self.__dataemissao
    def get_datavencimento(self): return self.__datavenc
    def get_valorboleto(self): return self.__valorboleto
    #def get_valor_pagamento(self): self.__valor
    def get_valorpago(self): return self.__valorpago
    def get_data_pagamento(self): self.__data_pagto
    def get_situacaopagamento(self): return self.__situacaopagamento
    def __str__(self):
        return f'Código de pagamento {self.__cod} | Data de emissão: {self.__dataemissao.strftime('%d/%m/%Y')} \n | Data de vencimento: {self.__datavenc.strftime('%d/%m/%Y')} | Valor do boleto: {self.__valorboleto:.2f} \n| Valor pago: {self.__valorpago:.2f} | Data de pagamento: {self.__data_pagto.strftime('%d/%m/%Y')} | Situação de pagamento {self.__situacaopagamento} |'
class BoletoUI:
    __boletos=[]
    @staticmethod
    def main():
        op=-1
        while op !=0:
            op=BoletoUI.menu()
            if op==1: BoletoUI.inserir()
            if op==2: BoletoUI.listar()
            if op==3: BoletoUI.atualizar()
            if op==4: BoletoUI.excluir()
            if op==5: BoletoUI.boletos_aberto()
            if op==6: BoletoUI.boletos_pago()
            if op==7: BoletoUI.boletos_vencer()
            if op==8: BoletoUI.boletos_vencido()
            if op==9: BoletoUI.pag_boletos()

    @staticmethod
    def menu():
        print('---------------------------------------------')
        print('1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir')
        print('5-Boletos em aberto, 6-Boletos pagos')
        print('7-Boletos a vencer, 8-Boletos vencidos')
        print('9-Pagar boltos, 0-FIm')
        print('---------------------------------------------')
        return int(input('Escolha uma das opções: '))
    @classmethod
    def inserir(cls):
        codbarras=input('Informe o código do boleto: ')
        dataEmissao=datetime.strptime(input('Informe a data de emissão dd/mm/aaaa: '), "%d/%m/%Y")
        datavencimento=datetime.strptime(input('Informe a data de vencimento dd/mm/aaaa: '), "%d/%m/%Y")
        valorboleto=float(input('Informe o valor: '))
        x=Boleto(codbarras, dataEmissao, datavencimento, valorboleto)
        cls.__boletos.append(x)
    @classmethod
    def listar(cls):
        for x in cls.__boletos:
            print(x)
    @classmethod
    def atualizar(cls):
        cod=int(input('Informe o ID: '))
        for t in cls.__boletos:
            if t.get_codbarras()==cod:
                dataEmissao=datetime.strptime(input('Informe a data de emissão dd/mm/aaaa: '), "%d/%m/%Y")
                datavencimento=datetime.strptime(input('Informe a data de vencimento dd/mm/aaaa: '), "%d/%m/%Y")
                valorboleto=float(input('Informe o valor: '))
                t.dataEmissao(dataEmissao)    
                t.datavencimento(datavencimento)
                t.valorboleto(valorboleto)
    @classmethod
    def boletos_vencido(cls):
        for x in cls.__boletos:
            if x.get_situacaopagamento() == Pagamento.EmAberto and \
            x.get_datavencimento()<datetime.now():
                print(x)
    @classmethod
    def excluir(cls):
        cod=input('Informe o código do boleto')
        for x in cls.__boletos:
            if x.get_codbarras() == cod:
                cls.__boletos.remove(x)
    @classmethod
    def boletos_aberto(cls):
        for x in cls.__boletos:
            if x.get_situacaopagamento() == Pagamento.EmAberto():
                print(x)
    @classmethod
    def boletos_pago(cls):
        for x in cls.__boletos:
            if x.get_situacaopagamento() == Pagamento.Pago():
                print('x')
    @classmethod
    def boletos_vencer(cls):
        for x in cls.boletos_aberto():
            if x.get_situacaopagamento() == Pagamento.Pago(): return
            else:
                if x.get_datavencimento()>datetime.now(): print(x)
    @classmethod
    def pag_boletos(cls):
        print('boleto para pagar: ')
        for x in cls.boletos_aberto():
            if x.get_situacaopagamento() == Pagamento.Pago(): return
            else: 
                print(x)
        valor=int(input('Informe o valor a ser pago: '))
        cod=input('Informe o código do boleto: ')
        for x in cls.__boletos:
            if x.get_codbarras() == cod:
                pg=x.pagar()-valor
                x.pagar(pg)
BoletoUI.main()