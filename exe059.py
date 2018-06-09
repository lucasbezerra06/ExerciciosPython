num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
op = 0
while op != 5:
    print('-=' * 20)
    op = int(input('''Escolha uma opção
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa
    --------------------:'''))
    print('-=' * 20)
    if op == 1:
        soma = num1 + num2
        print('A soma de {} com {} é {}'.format(num1, num2, soma))
    elif op == 2:
        mult = num1 * num2
        print('{} multiplicado por {} é {}'.format(num1, num2, mult))
    elif op == 3:
        if num1 > num2:
            print('{} é maior do que {}'.format(num1, num2))
        elif num1 < num2:
            print('{} é maior do que {}'.format(num2, num1))
        else:
            print('Os números são iguais')
    elif op == 4:
        num1 = int(input('Digite o 1º número: '))
        num2 = int(input('Digite o 2º número: '))
    elif op == 5:
        print('Saindo...')
    else:
        print('Opção invalida!')