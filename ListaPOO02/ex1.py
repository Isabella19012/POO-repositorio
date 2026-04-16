# Entidade
import math
class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2

class Circulo:
    def __init__(self):
        self.__raio=0.0
    def set_raio(self,r):
        if r >= 0: self.__raio = r
        else: raise ValueError()
    def  get_raio(self):
        return self.__raio
    def calculo_area(self):
        return math.pi*self.__raio**2
    def calc_circunferencia(self):
        return 2*math.pi*self.__raio


class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__horas = 0
        self.__minutos = 0
    def set_distancia(self, d):
        if d >= 0:
            self.__distancia = d
        else:
            raise ValueError()
    def set_horas(self, h):
        if h >= 0:
            self.__horas = h
        else:
            raise ValueError()
    def set_minutos(self, m):
        if 0 <= m < 60:
            self.__minutos = m
        else:
            raise ValueError()
    def get_distancia(self):
        return self.__distancia
    def get_horas(self):
        return self.__horas
    def get_minutos(self):
        return self.__minutos
    def calc_velocidade(self):
        tempo_total = self.__horas + (self.__minutos / 60)
        if tempo_total == 0:
            return "Tempo não pode ser zero"
        return self.__distancia / tempo_total

class conta_bancaria:
    def __init__(self):
        self.__saldo=0
        self.__nome=''
        self.__conta_numero=0
    def set_nome(self, n):
        self.__nome = n
    def set_numero(self, num):
        self.__conta_numero = num
    def get_numero_conta(self):
        return self.__conta_numero
    def get_nome(self):
        return self.__nome
    def get_numero(self):
        return self.__conta_numero
    def get_saldo(self):
        return self.__saldo
    def set_saldo(self,s):
        if s>=0: self.__saldo = s
        else: raise ValueError('Saldo menor que zero.')

    def calc_saldo(self, pergunta, sacar, depositar):

        if pergunta == 2: 
            if sacar <= self.__saldo:
                self.__saldo -= sacar 
            else:
                print("Saldo insuficiente")
        elif pergunta == 1:  
            self.__saldo += depositar
        return self.__saldo


class ingresso():
    def __init__(self):
        self.__dia = 0
        self.__hora = 0
    def set_hora(self,h):
        if 0 <= h <= 24:
            self.__hora = h
        else: raise ValueError()     
    def set_dia(self,d):
        if 1<=d<=7: self.__dia = d
        else: raise ValueError()
    def get_dia(self):
        return self.__dia
    def get_hora(self):
        return self.__hora
    def dia_semana(self):
        if 0 < self.__dia <= 7:

            # Definir valor base
            if self.__dia in [2, 3, 5]:  # Segunda, terça, quinta
                valorc = 16
            elif self.__dia == 4:        # Quarta
                return 8.0
            elif self.__dia in [6, 7, 1]:  # Sexta, sábado, domingo
                valorc = 20
            if 17 <= self.__hora <= 24:
                valorc += valorc * 0.5
            return float(valorc)
        else:
            return "Esse dia não existe"

# Interface com usuário (User Interface) - prints, inputs
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.Viagem()
            if op == 4: UI.conta_bancaria()
            if op == 5: UI.ingresso()

    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária 5-Ingresso 9-Fim")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def triangulo():
        print("Cálculo da área do triângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))     # método de instância
        x.set_altura(float(input("Informe o valor da altura: ")))
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")

    @staticmethod
    def circulo():
        print('Area e Circunferencia de um circulo')
        c=Circulo()
        c.set_raio(float(input('Digite o raio: ')))
        print(f'Área do circulo: {c.calculo_area()} e circunfêrencia: {c.calc_circunferencia()} ')
    @staticmethod
    def Viagem():
        print('Velocidade média da viagem.')
        v=Viagem()
        v.set_horas(int(input('Digite o tempo em horas: ')))
        v.set_minutos(int(input('Digite os minutos: ')))
        v.set_distancia(float(input('Digite a distância em KM: ')))
        print(f'Velocidade média da viagem: {v.calc_velocidade()}')
    @staticmethod
    def conta_bancaria():
        print('Conta bancária.')
        cb=conta_bancaria()
        cb.set_nome(input('Digite o seu nome: '))
        cb.set_numero(int(input('Digite o número da conta: ')))
        cb.set_saldo(float(input('Digite o seu saldo: ')))
        print('Depositar(1) Sacar(2)')
        pergunta=int(input('Deseja depositar ou sacar?:'))
        if pergunta==1:
            depositar=float(input('Quanto deseja depositar?:'))
            sacar =0
        elif pergunta ==2:
            sacar = float(input('Quanto deseja sacar?:'))
            depositar=0
        print(f'Titular: {cb.get_nome()} | número da conta: {cb.get_numero_conta()}')
        print(f'Seu saldo é de: {cb.calc_saldo(pergunta, sacar, depositar)}')
    @staticmethod
    def ingresso():
        c=ingresso()
        print('Domingo(1), Segunda(2), Terça(3), Quarta(4), Quinta(5), Sexta(6), Sábado(7).')
        c.set_dia(int(input('Informe o dia que irá para o cinema em número: ')))
        c.set_hora(int(input("Horário que irá: ")))
        print(f'Valor do ingresso: {c.dia_semana()}')
UI.main()