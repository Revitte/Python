# Desafio 13
# Faça um programa que leia o salario de um
# funcionario e mostre seu novo salario, com
# 15% de aumento.

print('Parabéns funcionario você '
      'recebeu um aumento de 15%\n')

sa = float(input('Informe seu salario atual.\n'
      'Salario atual: '))

s15 = sa + (sa * 0.15)

print('Seu novo salario é de {}'.format(s15))
