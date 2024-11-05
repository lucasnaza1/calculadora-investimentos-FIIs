from time import sleep
aplicacao_mensal = float(input('Digite o valor a ser aplicado mensalmente: '))
meses = int(input('Digite quantos meses você quer especular: '))
total_investido = aplicacao_mensal * meses
print('Calculando...')
sleep(1.2)
print('Aplicação no primeiro mês: R${:.2f}'.format(aplicacao_mensal))
print('Duração: {} meses'.format(meses))
print('Total investido em {} meses: R${:.2f}'.format(meses,total_investido))