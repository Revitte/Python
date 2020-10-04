# Desafio 11
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pinta-la,
# sabendo que cada litro de tinta, pinta uma área de dois metros quadrados.

l = float(input('Informe a largura da sua parede: '))
a = float(input('Informe a altura da sua parede: '))

area = (l * a)

ltrs = area / 4

print('Á area da sua parede é igual a {}\n'
      'e será necessario {} litros de   \n'
      'tinta para pintá-la'.format(area, ltrs))

