#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalahos dos alunos.
#Faça um progama que leia o nome dos quatros alunos e mostre a ordem sorteada
from random import sample
from time import sleep
print('\033[1;30m' '-=' *20)
print('\033[1;33m   GERADOR DE ORDEM PARA APRESENTAÇÃO')
print('\033[1;30m' '-=' * 20)
a = str(input('Digite o nome do aluno: ')).strip().capitalize()
b = str(input('Digite o nome do aluno: ')).strip().capitalize()
c = str(input('Digite o nome do aluno: ')).strip().capitalize()
d = str(input('Digite o nome do aluno: ')).strip().capitalize()
l = a, b, c, d
e = sample(l, k=len(l))
print('\033[1;31mAguarde...')
sleep(2)
print('\033[1;32mOrdem Sendo Gerada')
sleep(2)
print("\033[1;36mA ordem escolhida foi\n{}".format(e))
