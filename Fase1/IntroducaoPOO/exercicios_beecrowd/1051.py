salario = float(input())
if salario <= 2000:
    print('Isento')
elif salario <= 3000:
    imposto_a_pagar = (salario - 2000) * 0.08
    print(f'R$ {imposto_a_pagar:.2f}')
elif salario <= 4500:
    imposto_a_pagar = ((salario - 3000) * 0.18) + (1000 * 0.08)
    print(f'R$ {imposto_a_pagar:.2f}')
else:
    imposto_a_pagar = ((salario - 4500) * 0.28) + (1000 * 0.08) + (1500 * 0.18)
    print(f'R$ {imposto_a_pagar:.2f}')
