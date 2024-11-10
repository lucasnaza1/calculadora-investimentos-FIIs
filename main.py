from time import sleep
import math
aplicacao_mensal = float(input('Digite o valor a ser aplicado mensalmente: '))
valor_ativo = float(input('Qual o valor do ativo que pretende adquirir?'))
quantidade_cotas = int(aplicacao_mensal//valor_ativo)
rentabilidade_ativo = float(input('Quanto de dividendo, em média, o ativo está pagando?'))
meses = int(input('Digite quantos meses você quer especular: '))
taxa_de_crescimento = rentabilidade_ativo / valor_ativo
#A taxa de crescimento é baseado na rentabilidade do ativo sobre seu valor   
print('----'*20)
primeiro_mes = quantidade_cotas * rentabilidade_ativo
ultimo_mes = (quantidade_cotas * meses) * rentabilidade_ativo
total_investido = aplicacao_mensal * meses
saldo_final = total_investido * math.exp(taxa_de_crescimento * meses)
#O Saldo final é especulado com base no total aplicado por mês durante o período somando com a rentabilidade mensal exponencial durante o periodo
print('Calculando...')
print('----'*20)
sleep(1)
print('Aplicação no primeiro mês: R${:.2f}'.format(aplicacao_mensal))
print('----'*20)
print('Duração: {} meses'.format(meses))
print('----'*20)
print('Total investido em {} meses: R${:.2f}'.format(meses,total_investido))
print('----'*20)
print('Quantidade de cotas adquiridas por mês: {}'.format(quantidade_cotas))
print('----'*20)
print('quantidade de cotas adquiridas ao total: ', quantidade_cotas*meses)
print('----'*20)
print('Rendimento no primeiro mês: R${:.2f}'.format(primeiro_mes))
print('----'*20)
print('Rendimento no ultimo mês: R${:.2f}'.format(ultimo_mes))
print('----'*20)
print('Saldo total final: R${:.2f}'.format(saldo_final))
print('----'*20)
print('Levando em conta que não haverá reaplicação de verba!!!')

