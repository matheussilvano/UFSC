# Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
# 1 x N = N      2 x N = 2N        ...       10 x N = 10N
# 
# Entrada
# A entrada contém um valor inteiro N (2 < N < 1000).
# 
# Saída
# Imprima a tabuada de N, conforme o exemplo fornecido.

numero_entrada = int(input())
contador = 1
while contador <= 10:
    valor_final = numero_entrada * contador
    print(f'{contador} x {numero_entrada} = {valor_final}')
    contador +=1
