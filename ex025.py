#Crie um progama que leia um nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input('Digite seu nome: ')).strip()
print('O seu nome têm Silva:\n {}'.format('Silva' in nome.title()))
