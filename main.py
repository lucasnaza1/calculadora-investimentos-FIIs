from time import sleep
aplicacao_mensal = float(input('Digite o valor a ser aplicado mensalmente: '))
print('-----'*12)
valor_cota = str(input('Qual o valor atual de mercado da cota a ser adquirida?'))
print('-----'*12)
quantidade_cotas = aplicacao_mensal // valor_cota
print('-----'*12)
meses = int(input('Digite quantos meses você quer especular: '))
print('-----'*12)
total_investido = aplicacao_mensal * meses
print('Aplicação no primeiro mês: R${:.2f}'.format(aplicacao_mensal))
print('-----'*12)
print('Duração: {} meses'.format(meses))
print('-----'*12)
print('Total investido em {} meses: R${:.2f}'.format(meses,total_investido))