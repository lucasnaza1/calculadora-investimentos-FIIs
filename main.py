aplicacao_mensal = float(input('Digite o valor a ser aplicado mensalmente: '))
meses = int(input('Digite quantos meses você quer especular: '))
total_investido = aplicacao_mensal * meses
print('Aplicação no primeiro mês: {}\n Duração: {} meses \n Total investido em {} meses: {}'.format(aplicacao_mensal,meses,meses,total_investido))
