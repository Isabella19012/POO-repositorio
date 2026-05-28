from datetime import datetime
from enum import Enum
class Pagamento (Enum):
    EmAberto=1
    PagoParcial=2
    Pago=3
class Boleto:
    def __init__(self, codBarras, dataEmissao, datavencimento, valorboleto):
        #atributos que serão validados
        self.set_codbarras(codBarras)
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
        if dt_emissao > datetime.now: raise ValueError('impossivél.')
        self.__dataemissao=dt_emissao
    def set_datavencimento(self,venc):
        if venc < datetime.now: raise ValueError('Não se cria boleto vencido.')
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
        return f'Código de pagamento {self.__cod} | Data de emissão: {self.__dataemissao.strftime('%d/%m/%Y')} | Data de vencimento: {self.__datavenc.strftime('%d/%m/%Y')} | Valor do boleto: {self.__valorboleto:.2f} | Valor pago: {self.__valorpago:.2f} | Data de pagamento: {self.__data_pagto.strftime('%d/%m/%Y')} | Situação de pagamento {self.__situacaopagamento} |'
    