valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
anos = int(input('Em quantos anos ele vai pagar? '))
mes = anos * 12
prestacao = valor / mes
if prestacao <= (salario * 30 / 100):
    print('Valor da prestação pensal RS{:.2f} por {} meses'.format(prestacao, mes))
else:
    print('Emprestimo negado, valor de RS{:.2f} excede os 30% (RS{}) do salario'.format(prestacao, (salario * 30 / 100)))
