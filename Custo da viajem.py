# EX: preço da passagem, r$ 0.50 por km para até 200km, viajens mais logas r$0.45.
#distância = float(input('Qual é a distância da sua viajem?'))
#print('Voce está prestes a começar uma viajem de {}Km.'.format(distância))
#if distância <= 200:
#    preço = distância* 0.50
#else:
#    preço = distância* 0.45
#print('E o preço da sua passagem será de R${:.2f}'.format(preço))
# OU
distância = float(input('Qual é a distância da sua viajem?'))
print('Voce está prestes a começar uma viajem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))