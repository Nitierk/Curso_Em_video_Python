n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('DIgite sua segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Parabéns, você está acima da média, muito bem!')
else:
    print('Você está a baixo da média, estuda mais da proxima vez!')
