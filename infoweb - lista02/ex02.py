mes = 'none'
trimestre = 'primeiro'
Nmes = int(input('Informe o número do mês: '))
if Nmes > 0 and Nmes <= 12:
    if Nmes == 1:
        mes = 'Janeiro'
        trimestre = 'primeiro'
    elif Nmes == 2:
        mes = 'fevereiro'
    elif Nmes == 3:
        mes = 'março'
    elif Nmes == 4:
        mes = 'abril'
        trimestre = 'segundo'
    elif Nmes == 5:
        mes = 'maio'
        trimestre = 'segundo'
    elif Nmes == 6:
        mes = 'junho'
        trimestre = 'segundo'
    elif Nmes == 7:
        mes = 'julho'
        trimestre = 'terceiro'
    elif Nmes == 8:
        mes = 'agosto'
        trimestre = 'terceiro'
    elif Nmes == 9:
        mes = 'setembro'
        trimestre = 'terceiro'
    elif Nmes == 10:
        mes = 'outubro'
        trimestre = 'quarto'
    elif Nmes == 11:
        mes = 'novembro'
        trimestre = 'quarto'
    elif Nmes == 12:
        mes = 'dezembro'
        trimestre = 'quarto'

    print(f'O mês de {mes} é do {trimestre} trimestre do ano')
else: 
    print('Esse mês não existe')