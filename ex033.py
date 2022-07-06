"""Faça um programa que leia Três número e mostre qual é o maior e qual é o menor"""
#Recebendo os valores
n1 = float(input('1º Valor: '))
n2 = float(input('2º valor: '))
n3 = float(input('3º valor: '))
#Verificando quem é o menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor valor é {}'.format(menor))
#Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor é: {}'.format(maior))
