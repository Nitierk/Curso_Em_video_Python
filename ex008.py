"""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""
print('\033[1;32m''-=-'*10)
print('Transformador de Medidas')
print('-=-'*10)
n1 = float(input('\033[m''\033[1;34mDigite o valor em metros:'))
print('\033[mO valor em metros {} corresponde a\n{} km\n{} hm\n{} dam\n{} dm\n{} cm\n{} mm'
      .format(n1, n1 / 1000, n1 / 100, n1 / 10, n1 * 10, n1 * 100, n1 * 1000))
