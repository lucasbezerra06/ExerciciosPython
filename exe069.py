maior = homens = mulheres = 0
while True:
    print('=-' * 20)
    idade = int(input('Digite a idade: '))
    while True:
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M' or sexo == 'F':
            break
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1
    while True:
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if op == 'S' or op == 'N':
            break
    if op != 'S':
        break
print('=-' * 20)
print(f'''Foram cadastrados...
{maior} pessoas maiores de 18 anos.
{homens} homens.
{mulheres} mulheres menores de 20 anos.''')
