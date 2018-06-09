deis = vinte = cinquenta = um = 0
valor = int(input('Digite o valor a ser sacado: RS'))
valorSubtraido = valor

while True:
    if valorSubtraido == 0:
        break
    elif valorSubtraido - 50 >= 0:
        valorSubtraido -= 50
        cinquenta += 1
        if valorSubtraido - 50 < 0:
            print(f'{cinquenta} notas de R$50.00')
    elif valorSubtraido - 20 >= 0:
        vinte += 1
        valorSubtraido -= 20
        if valorSubtraido - 20 < 0:
            print(f'{vinte} notas de R$20.00')
    elif valorSubtraido - 10 >= 0:
        deis += 1
        valorSubtraido -= 10
        if valorSubtraido - 10 < 0:
            print(f'{deis} notas de R$10.00')
    elif valorSubtraido - 1 >= 0:
        um += 1
        valorSubtraido -= 1
        if valorSubtraido == 0:
            print(f'{um} notas de RS1.00')
print('=-' * 30)
print('Volte sempre, Tenha um bom dia!')
