#ansi - escape sequence-  \033[m] entre [ e o m coloque um codigo
#ex: \033[ stylo, text, back m - ex: \033[0;33;44m
#style - 0 none, 1bold, 4underline, 7negativo
#TEXT - 30white 31red 32gren 33yellow 34bleu 35purple 36oceano 37cinza
#BACK - 40      41    42     43       44     45      46       47
#ex: \033[0;33;41m
#ex: \033[4;33;44m
#ex: \033[m desfaz todas a configurações voltando ao padrao

#print('\033[31;43mOlá, mundo!\033[m')
#print('\033[34;47mOlá, mundo!\033[m')

#a = 3
#b = 5
#print('Os valores são \033[32m{}\033[m e \033[36m{}\033[m!!!'.format(a, b))

#nome = 'Borges'
#print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

#nome = 'Borges'
#cores = {'Limpa':'\033[m',
#         'Azul':'\033[34m',
#         'Amarelo':'\033[33m',
#         'Pretoebranco':'\033[7;30m'}

#print('Ola! Muito pazer em te conhecer, {}{}{}!!!'.format(cores['Pretoebranco'], nome, cores['Limpa']))
