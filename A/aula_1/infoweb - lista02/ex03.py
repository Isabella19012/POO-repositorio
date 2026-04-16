print('Valores entre 1 a 10 sem repetir.')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('terceiro valor: '))
d = int(input('Quarto valor: '))
lista = [a,b,c,d]
valido = True
if len(lista) != len(set(lista)):
    print("Tem valores repetidos")
    valido = False
else:
    for x in lista:
        if not (1 <= x <= 10):
            valido = False
            break
if valido:
    lista.sort()
    soma2 = lista[1] + lista[2]
    print('----------------')
    print('Maior valor: ',max(lista))
    print('Menor valor: ',min(lista))
    print('Soma segundo maior + segundo menor: ', soma2)
else:
    print('Entre 1 e 10.')