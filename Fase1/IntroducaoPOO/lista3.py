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
