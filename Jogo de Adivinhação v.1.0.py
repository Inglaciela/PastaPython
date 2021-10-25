from random import randint
from time import sleep
computador = randint(0, 8) #FAZ O COMPUTADOR "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 8. Tente adivinhar ...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) #JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')# tempo para o computador pensar "se quiser"
sleep(3)
if jogador == computador:
    print('PARABÉNS! Voce conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))