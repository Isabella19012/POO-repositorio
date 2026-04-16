dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

if ano>=1900 and ano>=2100:
    if 0>mes>=12:
        if dia >=31:
            print(f'{dia}/{mes}/{ano}')
    else: print('Mês inválido')
else: print('Ano inválido')