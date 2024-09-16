# Escreva um programa que leia o sexo das pessoas, mas somente aceite
# “M” ou “F”. Caso esteja errado, peça a digitação novamente até ter um valor
# correto. 

while True:
    sexo = input('Digite o sexo da pessoa (M/F): ').upper()
    if sexo == 'M' or sexo == 'F':
        print(f'O sexo selecionado foi {sexo}')
        break
    else:
        print('O sexo inserido é inválido')
