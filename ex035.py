#Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não forma um triângulo
print('-=' * 20)
print('As medidas podem formar um triangulo?')
print('-=' * 20)
m1 = float(input('Digite a primeira medida: '))
m2 = float(input('Digite a segunda medida: '))
m3 = float(input('Digite a terceira medida: '))
if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    print('Com as medidas {}, {} e {} É SIM POSSIVEL fazer um triangulo'.format(m1, m2, m3))
else:
    print('Com as medidas {}, {} e {} NÃO É POSSIVEl fazer um triangulo'.format(m1, m2, m3))
