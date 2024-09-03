# Escreva um programa para aprovar o empréstimo bancário para compra de uma
# casa. O programa vai perguntar o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela
# não pode exceder 30% do salário ou então o empréstimo será negado.

valor_da_casa = float(input('Qual o valor da casa?'))
salario_comprador = float(input('Qual o salário do comprador? '))
anos_para_pagar = float(input('Em quantos anos a casa vai ser paga? '))
parcela_maxima = salario_comprador * 0.3
parcela = valor_da_casa / (anos_para_pagar * 12)
if parcela > parcela_maxima:
  print('O comprador não pode comprar')
else:
  print('O comprador pode comprar')

# Elabore um programa que calcule o valor a ser pago por um produto, seu
#programa deve perguntar o valor do produto e a condição de pagamento.
# Considere:
# a. à vista (dinheiro ou cheque) – 10% de desconto
# b. 1x no cartão – 5% de desconto
# c. 2x cartão – preço normal
# d. 3x ou mais no cartão - 20% de juros
                  
