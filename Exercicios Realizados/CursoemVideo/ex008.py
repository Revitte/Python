# Desafio 008
# Escreva um programa que leia um
# valor em metros e o
# exiba convertido em
# centímetros e milímetros.

m = float(input('Me dê um valor em metros e eu \n'
      'converto em centímetros e milímetros:  '))

cm = m * 100
mm = m * 1000

print('{:.0f} metros é igual a {} centimetros\n'
      '{:.0f} metros é igual a {} milímetros'.format(m, cm, m, mm))
