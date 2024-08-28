entrada_segundos = int(input())
horas = entrada_segundos // 3600
tempo_restante_em_segundos = entrada_segundos % 3600
minutos = tempo_restante_em_segundos // 60
segundos = tempo_restante_em_segundos % 60
horario_completo_saida = print(f'{horas}:{minutos}:{segundos}')
