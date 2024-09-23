def verifica_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Contadores de pares e ímpares
cont_pares = 0
cont_impares = 0

# Lê 10 números inteiros
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: "))
    resultado = verifica_par_impar(numero)
    
    if resultado == "par":
        cont_pares += 1
    else:
        cont_impares += 1

# Exibe o resultado
print(f"Números pares: {cont_pares}")
print(f"Números ímpares: {cont_impares}")
