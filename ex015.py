"""Escreva um programa  que pergunte  a quantidade de Km percorridos por um carro alugado  e a quantidade  de dias pelos quais ele foi alugado.
   Calcule o preço a pagar.Sabendo que o carro custa R$ 60 por dia  e R$0.15 por Km rodado."""
print('\033[1;34m''-=' * 20)
print('VALOR COBRADO PELO ALUGUEL DO CARRO')
print('-=' * 20)
d = float(input('\033[1;36mQuantos dias o carro foi alugado? '))
k = float(input('Quants Km rodados com o carro? '))
print('\033[1;30m''=' * 35)
print('Quatidade de dias alugado:{} dias\nQuantidade de Km rodados:{}Km\nValor por dia:R$60\nValor por Km:R$0.15\nValor Total:R${}\nObrigado pela preferencia!'
      .format(d, k, (60 * d)+(0.15 * k)))
print('=' * 35)
