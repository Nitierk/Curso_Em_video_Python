#Faça um progama que leia um número inteiro e mostre seu sucessor e seu antecessor
print('\033[1;32m''-=' * 16)
print('Antecesor e Sucessor dos Número')
print('-=' * 16)
n1 = int(input('\033[1;34mDigite um número inteiro:'))
print('Procesando...')
print('\033[mO sucessor de {}{}{} é {}{}{}\nO antecessor de {}{}{} é {}{}{}'.format('\033[1;30m', n1, '\033[m',
                                                                          '\033[1;34m', n1+1, '\033[m',
                                                                          '\033[1;30m', n1, '\033[m',
                                                                          '\033[1;31m', n1-1, '\033[m'))
