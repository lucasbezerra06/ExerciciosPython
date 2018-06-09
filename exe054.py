from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasci = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    if anoAtual - nasci >= 21:
        maior += 1
    else:
        menor += 1
print('-=' * 20)
print('{} pessoas são maiores de idade'.format(maior))
print('{} pessoas NÃO são maiores de idade'.format(menor))
