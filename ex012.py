"""""Faça um Programa que receba um valor e dê 5% de desconto"""
print('\033[1;36m''-=-' * 10)
print('CALCULADORA 5% DE DESCONTO')
print('-=-' * 10)
p = float(input('\033[1;34mQual é o valor a ter o desconto: R$'))
print('\033[35mO valor R${} com o desconto de 5% fica valendo R${}'.format(p, p-(p*5/100)))
