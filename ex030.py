#Crie um programa que leia um numero inteiro e mostre na tela se ele é Par ou Impar
n = int(input('Digite qualquer número: '))
r = n % 2
if r == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é ÍMPAR'.format(n))
