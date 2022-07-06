'''Desenvolva um programa que pergunte a distância de uma viagem em KM
Calcule o preço da passagem.Cobrando
R$0,50 por KM para viagens de até 200Km e RS0,45 para viagens mais longas'''
v = float(input('Digite a distancia da viagem em Km: '))
if v <=200:
    print('Sobre a viagem com a distancia de {}Km\nSerá cobrado o valor de R${:.2f}'.format(v, (v * 0.5)))
else:
    print('Sobre a viagem com a distancia de {}Km\nSerá cobrado o valor de R${:.2f}'.format(v, (v * 0.45)))
