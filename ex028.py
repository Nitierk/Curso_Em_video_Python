#Escreva um programa que faça o computador "pensar" em um número entre 0 e 5
#E peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
#O programa devera escrever na tela se o usuário acertou ou não
from random import randint
from time import sleep
a = randint(0, 5) # Faz o computador pensar
print('-=-'* 10)
print('JOGO DA ADIVINHÇÂO')
print('-=-'* 10)
v = int(input('Tente adivinhar o número que o computador pensou\nDigite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if v ==a:
    print('Muito bem!Você acertou!')
else:
    print('Mais sorte da proxima vez!')
print('O número escolhido foi: {}'.format(a))
