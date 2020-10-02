# DESAFIO 03
#  um programa que leia dois numeros e mostre a soma entre eles!

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
s = n1 + n2

# print('A soma entre', n1, 'e', n2, 'vale', s)
# Uma sintaxe melhor para fazer o print:
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))

