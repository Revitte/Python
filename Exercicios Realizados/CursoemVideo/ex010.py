# Desafio 10
# Crie um programa que leia quanto dinheiro
# uma pessoa tem na carteira e mostre
# quantos dólares a ela pode comprar
# --
# Considere:
# US $ 1,00 = R$ 5,68
# Preço do dólar em 10/2020


print('-----------------------------------------\n'
      '!!SAIBA QUANTOS DÓLARES VOCÊ PODE TER!!\n'
      '_________________________________________\n')

print('(OBS: Não use vírgula!  \n'
      'caso queira informar os \n'
      'centavos use ponto.     \n'
      'exemplo: R$ "2250.35")  \n')

r = float(input('Pergunta: Quantos reais você tem? \n'
                'Resposta: R$ '))

d = r / 5.68

print('Você teria incriveis {:.2f} Dólares!!'.format(d))


