nome_vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())
porcentagem_vendas_15_porcento = total_vendas * 0.15

salario_com_comissao = salario_fixo + porcentagem_vendas_15_porcento
print(f'TOTAL = R$ {salario_com_comissao:.2f}')
