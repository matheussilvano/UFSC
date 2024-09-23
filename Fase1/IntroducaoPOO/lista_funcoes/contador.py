# 1) Faça um programa que tenha uma função chamada contador(), que tenha 3
# parâmetros: início, fim e passo, e realize a contagem. Seu programa terá que realizar 3
# contagens através da função criada.
# a) 1 a 10 de 1 em 1
# b) 10 a 0 de 2 em 2
# c) uma contagem personalizada

def contador(inicio, fim, passo):
    if passo == 0:
        print("O passo não pode ser zero!")
        return
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
    print()  # Para pular linha

print("Contagem de 1 a 10 de 1 em 1:")
contador(1, 10, 1)

print("Contagem de 10 a 0 de 2 em 2:")
contador(10, 0, 2)

# Contagem personalizada
print("Contagem personalizada:")
inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))
passo = int(input("Digite o passo: "))
contador(inicio, fim, passo)

