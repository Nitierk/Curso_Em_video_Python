#Escreva um programa que leia a velocidade de um carro
#SE ele utrapassar 80Km/h. Mostre uma mensagem dizendo que ele foi mutado
#A multa vai custar R$7,00 por cada Km acima do limite
v = float(input('Qual foi a velocidade do carro em Km/h? '))
if v >80:
    print('Você utrapassou a velocidade max permitida, que é 80 Km/h\nE Recebera uma muta no valor de R${:.2f}'.format((v - 80) * 7))
    print('Mais prudencia da proxima vez!')
print('Boa Viagem!')
