#Faça um progama que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
from time import sleep
print('\033[1;30m''-§-' * 13)
print('\033[1;36mCALCULADORA DE SENO, COSSENO, TANGENTE')
print('\033[1;30m-§-' * 13)
an = float(input('\033[1;34mDigite o ângulo que deseja: '))
cos = cos(radians(an))
sen = sin(radians(an))
tang = tan(radians(an))
print('\033[1;30m' '-=' * 20)
print('\033[1;35mO ângulo de {} tem o SENO de {:.2f}'.format(an, sen))
print('\033[1;33mO ângulo de {} tem o COSSENO de {:.2f}'.format(an, cos))
print('\033[1;32mO ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tang))
print('\033[1;30m' '-=' * 20)