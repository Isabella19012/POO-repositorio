# Entidade
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
        return 3.14*self.__raio**2
    def calc_circunferencia(self):
        return 2*3.14*self.__raio


class Viagem:
    def __init__(self):
        self.__distancia_K=0
        self.__tempo_H=0
    def get_distancia_K(self):
        return self.__distancia_K
    def get_tempo_H(self):
        return self.__tempo_H
    def set_distancia_K(self,k):
        if k>=0: self.__distancia_K = k
        else: raise ValueError()
    def set_tempo_H(self,k):
        if k>=0: self.__tempo_H = k
        else: raise ValueError()
    def calc_velocidade(self):
        return self.__distancia_K/self.__tempo_H
    
class conta_bancaria:
    def __init__(self):
        self.__saldo=0
    def get_distancia_K(self):
        return self.__saldo
    def set_saldo(self,s):
        if s>=0: self.__saldo = s
        else: raise ValueError('Saldo menor que zero.')

    def calc_saldo(self, pergunta, sacar, depositar):
        if pergunta == 1:
            if sacar <= self.__saldo:
                self.__saldo -= sacar 
            else:
                print("Saldo insuficiente")
        elif pergunta == 2:
            self.__saldo += depositar
        return self.__saldo

class ingresso:
    pass


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
        print(f"Um triângulo com base {x.get_base} e altura {x.get_altura} tem área = {area}")

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
        v.set_tempo_H(int(input('Digite o tempo em horas: ')))
        v.set_distancia_K(float(input('Digite a distância em KM: ')))
        print(f'Velocidade média da viagem: {v.calc_velocidade()}')
    @staticmethod
    def conta_bancaria():
        print('Conta bancária.')
        cb=conta_bancaria()
        nome=input('Digite o seu nome: ')
        numero_conta=int(input('Digite o número da conta: '))
        cb.set_saldo(float(input('Digite o seu saldo: ')))
        print('Depositar(1) Sacar(2)')
        pergunta=int(input('Deseja depositar ou sacar?:'))
        if pergunta==1:
            depositar=float(input('Quanto deseja depositar?:'))
            sacar =0
        elif pergunta ==2:
            sacar = float(input('Quanto deseja sacar?:'))
            depositar=0
        print(f'Titular: {nome} | número da conta: {numero_conta}')
        print(f'Seu saldo é de: {cb.calc_saldo(pergunta, sacar, depositar)}')
UI.main()