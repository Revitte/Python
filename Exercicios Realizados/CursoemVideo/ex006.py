# Desaio 6
# Crie um algoritimo que leia
# um número e mostre seu dobro,
# triplo e raiz quadrada.
# obs: Diferente do desafio anterior
# fiz esse input receber números float
# pois no desafio anterior se o tester
# digitar um numero com "." o programa da erro

print('Seja bem vindo ao desafio 6 meu querido tester')
v = float(input('Digite um valor: '))

dbr = v * 2
trpl = v * 3
rzq = v ** 2

print('O dobro do seu número é {0:.0f}\n'
      'O triplo do seu número é {1:.0f}\n'
      'e a raiz quadrada do seu numero é {2:.0f}'.format(dbr, trpl, rzq), end='')

# Ignore essa parte só tava testando o end=

print(' Testando o " end= "')

