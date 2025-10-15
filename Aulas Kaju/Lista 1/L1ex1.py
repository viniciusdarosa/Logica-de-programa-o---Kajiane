hora = float(input('Quantas horas você trabalha por mês? '))
ganho = float(input('Quantos você ganha por hora? '))

salarioB = hora*ganho

print(f'\n O salário Bruto foi R${salarioB}')
print(f'\n O valor pago pro INSS foi de R${salarioB*8/100}')
print(f'\n O valor pago pro sindicato foi de R${salarioB*5/100} ')
print(f'\n O valor do salário Liquido foi de R${(salarioB) - (salarioB*24/100)}')