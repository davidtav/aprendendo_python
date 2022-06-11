salario_mensal = input('digite o valor do seu salario mensal:  ')
salario_mensal = float(salario_mensal)

gasto_mensal = float(input('digite o valor do seu gasto mensal em média:  '))

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total
print('O montante que você pode economizar ao fim do ano é de:  ' , montante_economizado)