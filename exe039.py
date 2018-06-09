from datetime import date
nasci = int(input('Digite o seu ano de nascimento: '))
atual = int(date.today().year)
tempo = 18 - (atual - nasci)
if tempo > 0:
    print('Você ainda vai se alistar ao serviço militar, daqui a {} anos'.format(tempo))
    ano = atual + tempo
    print('Seu alistamento será em {}'.format(tempo))
elif tempo < 0:
    print('Voce já passou do tempo do alistamento, já se passaram {} anos'.format(tempo*(-1)))
    ano = atual - tempo*-1
    print('Seu alistametno foi em {}'.format(ano))
else:
    print('É a hora de se alistar')
