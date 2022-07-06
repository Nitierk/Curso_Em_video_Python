"""Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção intera."""
from math import trunc
print('\033[1;36mTRASFORMAÇÂO DA PORÇÃO INTEIRA\033[m')
n = float(input('\033[1;30m''Digite um número Real: '))
print('A porção inteira do número {} é {}'.format(n, trunc(n)))
