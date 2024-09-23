def calcular_media_e_melhor_nota(notas):
    media = sum(notas) / len(notas)
    melhor_nota = max(notas)
    return media, melhor_nota

# Notas dos 5 alunos
notas = []
for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

# Calcula a média e a melhor nota
media, melhor_nota = calcular_media_e_melhor_nota(notas)

# Determina o status do aluno com a melhor nota
if melhor_nota >= 5.75:
    status = "aprovado"
elif melhor_nota >= 2.75:
    status = "em recuperação"
else:
    status = "reprovado"

# Exibe os resultados
print(f"A média da turma é: {media:.2f}")
print(f"A melhor nota é: {melhor_nota:.2f}")
print(f"O aluno com a melhor nota está {status}.")
