# Desafio 007 em homenagem ao filme
# Desenvolver um programa que leia
# duas notas de um alune e calcule
# a sua média.

print('Seja bem vindo ao sétimo teste espião\n'
      'Um bom espião deve ter boas notas!!\n'
      '--------------------------------------')

n1 = int(input('Qual sua nota de 0 a 100\n'
          'na prova de furtividade?\n'
          'Resposta: '))
n2 = int(input('\n'
               'Qual sua nota de 0 a 100\n'
               'na prova de salto de paraquedas?\n'
               'Resposta: '))

med = (n1 + n2) / 2

print('Sua média como espião é: {:.1f}'.format(med))
