#Faça um progama que leia um ano qualquer e mostre se ele é um ano Bissexto
from datetime import date
print('Saiba se um ano é Bissexto ou não')
n = int(input('Digite um ano qualquer, ou caso queira analisar o ano atual digite 0: '))
if n == 0:
    n = date.today().year
if (n % 4) == 0 and n % 100 != 0 or n % 400 == 0:
    print('{} é um ano Bissexto'.format(n))
else:
    print('{} não é um ano Bissexto'.format(n))
