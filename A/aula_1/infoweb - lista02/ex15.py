#versao sem função
numero = int(input('digite um número inteiro: '))
primo = True
for d in range(2, numero):                 #basta a raiz quadrada
    if numero % d == 0: primo = False
    if primo == False: break               #if not primo:
if primo == True: print(numero,'é primo')  #if primo:
else: print(numero,'não é primo')
#versao função
def primo(numero):
    primo = True
    for d in range(2, numero):                 #basta a raiz quadrada
        if numero % d == 0: primo = False
        if primo == False: break           
    return primo

numero = int(input('digite um número inteiro: '))
if primo(numero): print(numero,'é primo')  #if primo:
else: print(numero,'não é primo')