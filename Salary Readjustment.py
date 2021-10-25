salário = float(input('Qula é o salario do funcionario?R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 25% de aumento, passa a recebr R${:.2f}'.format(salário, novo))
