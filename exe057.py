s = str(input('Digite o seu sexo [M/F]:' )).strip().upper()[0]
while s not in 'MF':
    s = str(input('Opção invalida, Ditite o seu sexo [M/F]: ')).strip().upper()[0]
print('Seu sexo é masculino' if s == 'M' else 'Seu sexo é feminino')

