#Crie um progama que leia o nome de uma cidade  e diga se ela começa ou não com o nome 'Santo'
nome = input('Digite o nome de uma cidade')
a = nome.strip().split()[0]
s = a.capitalize()
print('O nome da cidade indicada tem Santo no inicio:\n{}'.format('Santo' in s))