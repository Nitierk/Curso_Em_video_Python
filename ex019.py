#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um progama que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
from time import sleep
print('\033[1;30m' '-=' * 15)
print('\033[1;32m' '  SELETOR ALEATÓRIO DE ALUNO')
print('\033[1;30m' '-=' * 15)
print('\033[1;31mIniciando Agarde...')
sleep(3)
print('\033[1;32mPrograma Carregado\033[m')
a = str(input('\033[30mNome de um dos alunos: ')).strip().capitalize()
b = str(input('Nome de um dos alunos: ')).strip().capitalize()
c = str(input('Nome de um dos alunos: ')).strip().capitalize()
d = str(input('Nome de um dos alunos: ')).strip().capitalize()
e = choice(seq=(a, b, c, d))
print('O aluno escolhido aleatoriamente foi...')
sleep(3)
print('\033[1;36m{}'.format(e))