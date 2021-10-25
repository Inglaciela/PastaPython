# PAR :0, RESTO DA DIVISAO DE QUALQUER NÚMERO PAR POR DIVIDIDO 2 VAI DAR 0
# IMPAR :1, RESTO DA DIVISAO DE QUALQUER NÚMERO IMPAR DIVIDIDO POR 2 VAI DAR 1
número = int(input('Me diga um número qualquer:'))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é IMPAR'.format(número))