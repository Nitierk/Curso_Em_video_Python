"""Faça um algoritimo que leia o salário de um funcionário
   E mostre seu novo salário, com 15% de aumento."""
print('\033[1;34m''-=' * 16)
print('CALCULADORA DE AUMENTO SALARIAL')
print('-=' * 16)
s = float(input('\033[36mQual é o valor do salário que será reajustado: R$ '))
a = int(input("Qual o valor da porcentagem de aumento:"))
print('\033[35mO salário de R${} com o aumento de {}% fica de R${}'.format(s, a, s+(s * a /100)))
