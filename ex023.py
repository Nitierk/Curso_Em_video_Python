"""Faça um progama que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
EX:
Digite um número: 1834
Unidade:4
Dezenas:3
Centenas:8
Milhar:1"""
num = int(input('Digite um número entre 0 e 9999: '))
print('Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}\n'
      .format(num // 1 % 10,
              num // 10 % 10,
              num // 100 % 10,
               num // 1000 % 100))
