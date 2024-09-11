# Escreva um programa que imprima todos os anos bissextos do século XXI.
# Lembre-se que o primeiro ano bissexto do século foi em 2004 e que o último será
# em 2096 e que os anos bissextos ocorrem usualmente de 4 em 4 anos.

ano = 2000
lista_anos = []
while ano <2100:
    if ano % 4 == 0:
        lista_anos.append(ano)
    ano += 1
print(lista_anos)

# Faça um programa que imprima na tela apenas os números ímpares entre 1 e
# 50.

numero = 1
while numero < 50:
    if numero % 2 != 0:
        print(numero)
    else:
        ...
    numero += 1

# Uma universidade particular oferece um desconto de 30% na mensalidade do
# aluno com melhor nota (média geral). Implemente um programa que após
# receber as informações do aluno (nome, nota/média geral, valor mensalidade)
# verifique quem é o aluno com melhor nota e calcule o desconto de sua
# mensalidade.
# Ao final de sua execução, o programa deve mostrar:
# - o nome do aluno com melhor nota,
# - o valor da mensalidade (sem desconto) e
# - o valor da mensalidade com o desconto e 30%;
# Considerar 5 alunos (as informações devem ser lidas do teclado), considerar
# alunos com notas distintas.

contador = 0
nota = 0
while contador <= 5:
    novo_nome_aluno = input('Digite o nome do aluno: ')
    novo_valor_mensalidade = float(input('Insira o valor da mensalidade: '))
    nova_media_geral = float(input('Digite a média do aluno: '))
    if nova_media_geral > nota:
        nota = nova_media_geral
        valor_mensalidade = novo_valor_mensalidade
        nome_aluno = novo_nome_aluno
    else:
        ...
    contador += 1
valor_com_desconto_mensalidade = valor_mensalidade * 0.7
print(f'O melhor aluno {nome_aluno}, reduzirá sua mensalidade de R${valor_mensalidade} para R${valor_com_desconto_mensalidade}.')

# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade
# de números pares e a quantidade de números impares.

contador = 0
contador_pares = 0
contador_impares = 0
while contador < 10:
    numero = int(input('Digite um número inteiro: '))
    contador += 1
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
print(f'''Números pares: {contador_pares}
Números ímpares: {contador_impares}''')
