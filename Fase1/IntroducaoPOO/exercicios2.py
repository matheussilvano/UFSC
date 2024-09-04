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

print('===== CALCULADORA DE PREÇO =====')
valor_produto = float(input('Insira o valor do produto: '))

while True:
    modalidade_pagamento = input('''[1] Dinheiro ou cheque
    [2] 1x no cartão
    [3] 2x no cartão
    [4] 3x ou mais no cartão
    Insira a modalidade do pagamento: ''')
    if modalidade_pagamento == '1':
        preco_final = valor_produto - (valor_produto * 0.1)
        break
    elif modalidade_pagamento == '2':
        preco_final = valor_produto - (valor_produto * 0.05)
        break
    elif modalidade_pagamento == '3':
        preco_final = valor_produto
        break
    elif modalidade_pagamento == '4':
        preco_final = valor_produto + (valor_produto * 0.2)
        break
    else:
        print('Esse valor não é valido.')
print(f'O valor final do produto é R$ {preco_final:.2f}')


# Desenvolva um algoritmo que leia o peso e altura de uma pessoa, calcule seu IMC
# e mostre seu status de acordo com:
# Abaixo de 18,5 – abaixo do peso
# Entre 18.5 e 25 – peso ideal
# Entre 25 e 30 - sobrepeso
# Entre 30 e 40 - obesidade
# Acima de 40 - obesidade mórbida
# Para o cálculo do IMC, considere: IMC = peso / (altura x altura)

altura = int(input('Insira sua altura em cm: '))
peso = float(input('Insira seu peso em Kg: '))
imc = float(peso/(altura/100)**2)
if imc < 18.5:
    print(f'Seu imc é {imc:.2f} e você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print(f'Seu imc é {imc:.2f} e você está no peso ideal.')
elif 25 < imc <= 30:
    print(f'Seu imc é {imc:.2f} e você está com sobrepeso.')
elif 30 < imc <= 40:
    print(f'Seu imc é {imc:.2f} e você está na situação de obesidade.')
else:
    print(f'Seu imc é {imc:.2f} e você está na situação de obesidade mórbida.')

# Faça um programa que leia 3 notas de um aluno, calcule sua média e mostre seu
# conceito final conforme a indicação abaixo:
# Abaixo de 5 – Reprovado
# Entre 5 e menor que 7 – Em recuperação
# Igual ou maior que 7 – Aprovado

nota1 = float(input('Insira a primeira nota do aluno (1/3): '))
nota2 = float(input('Insira a segunda nota do aluno (2/3): '))
nota3 = float(input('Insira a terceira nota do aluno (3/3): '))
media = (nota1 + nota2 + nota3) / 3
if media < 5:
    print(f'A média do aluno foi {media:.2f}, então ele foi reprovado.')
elif 5 <= media < 7:
    print(f'A média do aluno foi {media:.2f}, então ele está em recuperação.')
else:
    print(f'A média do aluno foi {media:.2f}, então ele foi aprovado.')
