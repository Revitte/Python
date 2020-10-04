# Desafio 005
# Faça um programa que leia um número
# inteiro e mostre na tela o seu
# sucessor e seu antecessor.

print('Seja bem vindo a mais um desafio')
n = int(input('Escreva um número "REI" >>>  '))

su = n + 1
an = n - 1

print('O sucessor de seu número será! {0} \n'
      'O antecessor de seu número será! {1}'.format(su, an))
