# Desafio 12
# Faça um algoritmo que leia o preço de um
# produto e mostre seu novo preço, com 5% de
# desconto.

p = float(input('Qual o valor do seu produto?\n'
            'RESPOSTA: '))

p5 = p - (p * 0.05)

print('Seu produto com 5% de desconto custaria: {} '.format(p5))