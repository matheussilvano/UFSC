pessoas = []

# Cadastro das pessoas
while True:
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    peso = float(input("Digite o peso da pessoa (em kg): "))

    # Adiciona a pessoa à lista
    pessoas.append([nome, idade, peso])

    # Verifica se o usuário deseja continuar cadastrando
    continuar = input("Deseja continuar cadastrando? (s/n): ").strip().upper()
    if continuar != 'S':
        break

# 1.1 Quantidade de pessoas cadastradas
quantidade_de_pessoas = len(pessoas)
print(f"Total de pessoas cadastradas: {quantidade_de_pessoas}")

# 1.2 Pessoa(s) mais pesada(s)

peso_maximo = max(pessoa[2] for pessoa in pessoas)
mais_pesadas = [pessoa for pessoa in pessoas if pessoa[2] == peso_maximo]
print("\nPessoa(s) mais pesada(s):")
for pessoa in mais_pesadas:
    print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}, Peso: {pessoa[2]} kg")

# 1.3 Pessoa(s) mais leve(s)
if pessoas:
    peso_minimo = min(pessoa[2] for pessoa in pessoas)
    mais_leves = [pessoa for pessoa in pessoas if pessoa[2] == peso_minimo]
    print("\nPessoa(s) mais leve(s):")
    for pessoa in mais_leves:
        print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]}, Peso: {pessoa[2]} kg")

# 1.4 Pessoas com mais de 20 anos
pessoas_acima_20 = [pessoa for pessoa in pessoas if pessoa[1] > 20]
print("\nPessoas acima de 20 anos:")
if pessoas_acima_20:
    for pessoa in pessoas_acima_20:
        print(f"Nome: {pessoa[0]}, Idade: {pessoa[1]} anos")
else:
    print("Nenhuma pessoa cadastrada com mais de 20 anos.")
