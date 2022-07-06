#Faça um progama que leia um frase e e mostre:
#Quantas vezes aparece a letra "a'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez
frase = str(input('Digite uma frase qualquer:')).lower().strip()
print('A frase tem quantos "A"s: {}'.format(frase.count('a')))
print('A primeira letra "A" aparece na posição: {}'.format(frase.find('a')+1))
print('A ultima letra "A" aparece na posição: {}'.format(frase.rfind('a')+1))
