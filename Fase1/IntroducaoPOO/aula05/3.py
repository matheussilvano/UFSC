# 3) Implementar um programa que calcula o desconto previdenciário dos
# funcionários de uma empresa. O algoritmo deve, dado um salário, retornar o
# valor do desconto proporcional ao mesmo.
# - O cálculo de desconto segue a seguinte regra: o desconto deve ser de
# 11% do valor do salário, entretanto, o valor máximo de desconto é R$320,00.
# Sendo assim, seu programa deve verificar se calculará sobre 11% do salário
# ou utilizará o teto R$320,00. No caso, de o desconto aplicado for R$320,00,
# seu programa deve indicar qual foi o % de desconto aplicado para este
# funcionário.
# - Critério de parada definido pelo usuário (perguntar a cada verificação
# se deseja continuar)

salario = 1
while salario != 0:
    salario = float(input('Digite o salário do funcionário (ou 0 para parar): '))
    desconto = salario * 0.11
    if desconto <= 320:
        print(f'O desconto realizado foi de 11%, totalizando R${desconto}')
    else:
        desconto = 320
        porcentagem_descontada = (320/salario) * 100
        print(f'O desconto realizado foi de {porcentagem_descontada}%, totalizando R${desconto}')
print('Finalizado')

