def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def contar_primos(inicio, fim):
    contagem = 0
    for numero in range(inicio, fim + 1):
        if eh_primo(numero):
            contagem += 1
    return contagem

# Solicita ao usuário os limites do intervalo
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

# Conta os números primos no intervalo
quantidade_primos = contar_primos(inicio, fim)

# Exibe o resultado
print(f"A quantidade de números primos no intervalo [{inicio}, {fim}] é: {quantidade_primos}")
