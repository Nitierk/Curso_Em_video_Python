""""Faça um progama que leia a largura e a altura de uma parede em metros
Calcule a sua área e a quantidade de tinta necessaria para pinta-la
Sabendo que cada litro de tinta, pinta uma área de 2m"""
print('\033[1;36m''-=' * 10)
print('CALCULADORA DE TINTA')
print('-=' * 10)
a = float(input('\033[1;34m''Digite o valor da altura em metros: '))
l = float(input('Digite o valor da largura em metros: '))
aa = a * l
print('\033[m''\033[1;35mA área da parede as quais as dimenssões são {}x{} é {}m²\nSerá necessario {}L de tinta para pintar {}m²'.format(l, a, aa, aa/2, aa))
