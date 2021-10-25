velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('MULTADO! Voce execedeu o limite permitido que é 80km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
#calculo conforme a velocidade "80" e multa por km "7" ex: