"""Escreva um programa que  converta uma temperatura digitada em ºC e converta para ºF"""
print('\033[1;34m''-=' * 12)
print('CONVERSO DE TEMPERATURA')
print('-=' * 12)
c = float(input('\033[1;36mDigite a temperatura em graus ºC:'))
print('\033[1;30mA temperatura em Celsius {} convertida para ºF é {}'
      .format(c, ((9 * c) / 5) + 32))
