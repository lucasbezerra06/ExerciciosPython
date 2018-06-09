res = True
media = 0
cont = 0
maior = 0
menor = 0
while res:
    cont += 1
    n = int(input('Digite um número inteiro: '))
    media += n
    if cont == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    op = input('Deseja continuar? [S/N]').upper().strip()[0]
    if op in 'Nn':
        res = False
media /= cont
print('Media: {}\nMaior: {}\nMenor: {}'.format(media, maior, menor))
