from random import randint
vitorias = 0
while True:
    comp = randint(0, 10)
    escolha = str(input('Escolha Par ou Impar: ')).strip().upper()[0]
    jogador = int(input('Digite um número:'))
    print(f'Você escolheu {escolha} e jogou {jogador} e o computador jogou {comp}')
    soma = jogador + comp
    if (escolha == 'P' and soma % 2 == 0) or (escolha == 'I' and soma % 2 != 0):
        print('Você veunceu!')
        print('=-' * 20)
        vitorias += 1
    else:
        print('Você perdeu!')
        print('=-' * 20)
        break
print(f'Você veu {vitorias} vezes seguidas!')
