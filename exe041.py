from datetime import date
nasci = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nasci
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
