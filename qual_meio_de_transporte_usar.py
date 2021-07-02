
valor_passagem = 4.50

valor_corrida = float(input('Qual é o valor da corrida ?  '))

if valor_corrida <= valor_passagem * 4:
    print('Pague a corrida')
elif valor_corrida <= valor_passagem * 5:
    print('Espere um pouco, o valor da corrida pode abaixar')
else:
    print('Pegue o ônibus')