#import datetime ou from datetime import datetime.(o primeiro é modulo, o segundo é classe)
# strptime - passa de string para datetime -  método estático - chhama uma classe
# strftime- passa de datatime para string "s%/m%/Y%" - método de instância - chama com uma variável.
#timedelta - intervalo de tempo
from datetime import datetime, timedelta
nasc=datetime.strptime(input("Informe a data do seu nascimento: "), "%d/%m/%Y")
hoje=datetime.now()
z=hoje-nasc # intervalo de tempo entre hoje e a data de nascimento.
print(z)
anos = z.days//365
print(anos)
x.days % 365 #dias restantes
meses=x.days % 365 //30 #meses restantes
print(meses)