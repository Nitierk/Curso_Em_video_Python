#Faça com que o progama leia algo do seu teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele
i = input('Digite qualquer coisa:')
print('O tipo primitivo desse valor é {}!'.format(type(i)))
print('É somente espaço?', i.isspace( ))
print('É númerico?', i.isnumeric( ))
print('É alfabético?', i.isalpha())
print('É aplfanúmerico?', i.isalnum())
print('Está escrito somente em minúsculo?', i.islower())
print('Está escrito somente em maiúsuclo?', i.isupper())
print('Está capitalizada?', i.istitle())

