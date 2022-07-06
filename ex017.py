#Faça um progama que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo rêtangulo.
#Calcule e mostre o comprimento da hipotenusá
'''from math import sqrt
o = float(input('Digite o valor do comprimento do Cateto Oposto:'))
a = float(input('Digite o valor do comprimento do Cateto Adjacente: '))
h = 2 ** o + 2 ** a
print('o Cateto O. vale {}\n O Cateto Adj. vale {}\nCom isso chegamos ao valo da Hiptenusá que é {}'
      .format(o, a, sqrt(h))
co = float(input('Digite o Valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
'''Tudo errado acima'''
print('\033[1;34m''-=' * 15)
print('Calculadora de Hipotenusa')
print('-=' * 15)
from math import hypot
co = float(input('\033[1;31mDigite o valor do cateto oposto: '))
ca = float(input('\033[1;33mDigite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print('\033[1;35mO valor da hipotenusa é {:.2f}'.format(hi))
