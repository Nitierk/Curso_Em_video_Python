"""Faça um algoritimo que calcule o desconto de 10% do valor de um produto ao ser comprada a vista
   E calcule também o preço dele com um aumento de 8% no valor a ser comprado a prazo"""
print('\033[1;36m''-=' * 10)
print('MAQUINA DE PAGAMENTO')
print('-=' * 10)
v = float(input('\033[1;34mDigite o valor do produto: R$'))
print('\033[1;32mO produto tem o valor de {:.2f}\nEscolha sua forma de pagamento:\nÀ vista: R${:.2f}\n À prazo:'.format(v, v -(v * 10 / 100)))
print('\033[1;30mx2: R${:.2f}\nx3: R${:.2f}\nx4: R${:.2f}\nx5: R${:.2f}\nx6: R${:.2f}\nx7: R${:.2f}\nx8: R${:.2f}\nx9: R${:.2f}\nx10: R${:.2f}\nx11: R${:.2f}\nx12: R${:.2f}'
      .format(v + (v * 8 / 100), v + 2 *(v * 8 / 100), v + 3 *(v * 8 / 100), v + 4 * (v * 8 / 100), v + 5 *(v * 8 /100),
              v + 6 * (v * 8 / 100), v + 7 * (v * 8 / 100), v + 8 * (v * 8 / 100), v + 9 * (v * 8 / 100), v + 10 * (v * 8 / 100),
              v + 11 * (v * 8 / 100), v + 12 * (v * 8 / 100)))
