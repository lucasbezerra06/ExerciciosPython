from random import randint
vitorias = 0
while True:
    comp = randint(0, 10)
    while True:
        escolha = str(input('Escolha Par ou Impar: ')).strip().upper()[0]
        if escolha in 'PpIi':
            break
    jogador = int(input('Digite um número: '))
    soma = jogador + comp
    print(f'Você escolheu {escolha} e jogou {jogador} e o computador jogou {comp}, e a soma dos dois números é {soma}')
    print('Deu Par' if soma % 2 == 0 else 'Deu Impar')
    if (escolha == 'P' and soma % 2 == 0) or (escolha == 'I' and soma % 2 != 0):
        print('Você veunceu!')
        print('=-' * 20)
        vitorias += 1
    else:
        print('Você perdeu!')
        print('=-' * 20)
        break
print(f'Você veu {vitorias} vezes seguidas!')
