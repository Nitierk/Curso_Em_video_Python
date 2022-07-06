"""Crie um progama que leia dois números e mostre a soma entre eles."""
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
s = n1+n2
print('A soma entre {}{}{} e {}{}{} é {}{}{}!'
      .format('\033[33m', n1, '\033[m', '\033[33m', n2, '\033[m', '\033[34m', s, '\033[m'))
