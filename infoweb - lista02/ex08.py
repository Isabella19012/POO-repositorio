palavra = input('Palavra: ')
x=0
letra = palavra[x]
print(' ')
for letra in range(len(palavra)):
    palavra = palavra[1:] + palavra[0]
    print(palavra)