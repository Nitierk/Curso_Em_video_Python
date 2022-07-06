#Escreva um programa que pergunte um sálario de um funcionário e calcule o valor do seu aumento
#Para sálarios superiores a R$1.250,00, calcule um aumento de 10%
#Para o Inferiores ou iguais, o aumento é de 15%
print('Calculadora de aumento!')
s = float(input('Digite o sálario atual do funcionario: R$'))
if s > 1250.00:
    print('O sálario do funcionario atualmente é R${:.2f}\nCom o aumento de 10%, se tornará R${:.2f}'.format(s, s * 10 / 100 + s))
else:
    print('O sálario do funcionário atualmente é R${:.2f}\nCom o aumento de 15%, se tornará R${:.2f}'.format(s, s * 15 / 100 + s))
