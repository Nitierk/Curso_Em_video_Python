#Desenvolva um progama que leia as duas notas de um aluno, calcule e mostre sua média.
print('\033[1;32m''-=-' * 7)
print('Calculadora de Média')
print('-=-' * 7)
n1 = float(input('\033[m''\033[1;34mPrimeira Nota:'))
n2 = float(input('Segunda Nota:'))
print('\033[mA media entre as notas {}{}{} e {}{}{} é {}{:.2f}{}'.format('\033[1;33m', n1, '\033[m',
                                                                         '\033[1;33m', n2, '\033[m',
                                                                         '\033[1;36m', (n1+n2)/2, '\033[m'))

