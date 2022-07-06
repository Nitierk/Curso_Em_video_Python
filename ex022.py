"""Crie um progama que leia o nome completo de um pessoa e:
   O nome com todas as letras em maiúsculas
   O nome com todas letras em minúsculas
   Quantas letras ao todo (sem contar com os espaços)
   Quantas letras tem o primeiro nome"""
from time import sleep
print('\033[1;30m' '-=' * 11)
print(' \033[1;36;40mANALASIDOR DE NOMES\033[m')
print('\033[1;30m''-=' * 11)

print('\033[1;32mIniciado programa...')
sleep(3)
#Tela de Inicialização

nome = str(input('\033[1;36mDigite seu nome completo: ''\033[1;35m')).strip()
     #Recebendo Nome do Usuario
print('Seu nome com todas as letras em maiúsculas: {}\n'
      'Seu nome com todas as letras em minúsuculas: {}\n'
      'Seu nome completo tem o total de {} letras\n'
      'Seu primeiro nome é {} e tem {} letras'
      .format(nome.upper(), nome.lower(),
      len(nome) - nome.count(' '),nome.split()[0], len(nome.split()[0])))
      #Mostrando resultado para ususario