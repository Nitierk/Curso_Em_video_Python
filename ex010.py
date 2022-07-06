"""Crie um programa que leia quanto dinheiro  uma pessoa tem na carteira
E mostre quantos dólares, euros e libras ela pode compra
Considere: U$1,00 = R$5,05, €1,00 = R$5,68, ‎£1 = R$6,33"""
print('\033[1;32m''-=' * 10)
print('Converso de Moedas')
print('-=' * 10)
n = float(input('\033[m''\033[1;36mDigite o valor que você tem na sua carteira:R$'))
print('\033[m''Você tem R${:.2f} e pode comprar:\nDólares: U${:.2f}\nEuros: €{:.2f}\n‎Libras: £{:.2f}'.format(n, n / 5.39, n / 6.42, n /7.20))
