#Faça um progama que leia um nome completo de uma pessoa, mostrando o primeiro e o ultimo nome separadamente
#EX: Ana Maria de Souza
#primeiro nome: Ana
#ultimo nome: Souza
nome = str(input('Digie=te seu nome completo: ')).title().strip().split()
print('O seu primeiro nome é: {}'.format(nome[0]))
print('O seu ultimo nome é: {}'.format(nome[len(nome)-1]))
