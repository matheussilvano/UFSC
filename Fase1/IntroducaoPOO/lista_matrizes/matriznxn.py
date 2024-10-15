# 5) Crie um programa que crie uma matriz de dimensão nxn (n lido do teclado) e preencha com
# valores lidos pelo teclado.
# a) Mostre a soma de todos os elementos pares da matriz
# b) Mostre a média dos elementos da diagonal principal
# c) Mostre o produto dos elementos da diagonal secundária
# d) Mostre a média dos elementos acima da diagonal principal
# e) Mostre a soma dos elementos da última coluna da matriz
# f) Mostre o menor valor da primeira linha da matriz
# Importante: a matriz deve ser impressa na tela com formatação correta 

numero_de_linhas_e_colunas = int(input('Insira o "n" para a matriz (nxn): '))
matriz = []
soma_pares = 0
print('=== Valores da Matriz ===')
for i in range (numero_de_linhas_e_colunas):
    linha = []
    for j in range (numero_de_linhas_e_colunas):
        valor = int(input(f'Digite o dígito [{i+1},{j+1}]: '))
        linha.append(valor)
        # Calcula a soma dos números pares
        if valor % 2 == 0:
            soma_pares += valor     
    matriz.append(linha)

# Printa a soma dos pares na tela
print(f'A soma dos números pares da matriz é: {soma_pares}.')

# Elementos da diagonal principal
contador_diagonal_principal = 0
soma_diagonal_principal = 0
while contador_diagonal_principal < numero_de_linhas_e_colunas:
    soma_diagonal_principal += matriz[contador_diagonal_principal][contador_diagonal_principal]
    contador_diagonal_principal += 1
media_diagonal_principal = soma_diagonal_principal / numero_de_linhas_e_colunas
print(f'A média da diagonal principal é: {media_diagonal_principal}')

# Elementos da diagonal secundária
contador_diagonal_secundaria = numero_de_linhas_e_colunas-1
multiplica_diagonal_secundaria = 1
while contador_diagonal_secundaria >= 0:
    multiplica_diagonal_secundaria *= matriz[contador_diagonal_secundaria][contador_diagonal_secundaria]
    contador_diagonal_secundaria -= 1
print(f'O produto da diagonal secundária é: {multiplica_diagonal_secundaria}')
print(matriz)
