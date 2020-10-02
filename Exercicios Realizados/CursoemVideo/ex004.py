# DESAFIO 4
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possiveis sobre ele.

#A maneira como eu fiz:
n = input('Digite algo: ')
print('O que você digitou é do tipo: {}'.format(type(n)))
print('O que você digitou pode ser considerado um número inteiro? {}!'.format(n.isnumeric()))
print('Um numero real? {}!'.format(n.isnumeric()))
print('Um valor alfabetico? {}! '.format(n.isalpha()))
print('Um valor alfanumerico? {}! '.format(n.isalnum()))
print('Um espaço? {}!'.format(n.isspace()))


