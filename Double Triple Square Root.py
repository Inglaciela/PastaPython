n = int(input('Didite um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}.A raiz quadrada de {} é igual a {}.'.format(n, t, n, r))
# OU PARA FAZER DIRETO
#COLOCAR \n ANTES DE .a raiz, PARA QUEBRA DE LINHA
#NA NO (d) DA LINHA 5 COLOCAR (n*2)))
#NO {} DA RAIZ QUADRADA COLOCAR {:.2F} PARA 2 CASA DECIMAIS FLOAT
#NO LUGAR DO t DA LINHA 6 COLOCAR (N*3)
#NO LUGAR DO r DA LINHA 6 COLOCAR (N**(1/2))))
#AINDA PARA CALCULAR A RAIZ QUADRADA DA LINHA 6 COLOCAR pow(n, (1/2))))