import datetime
dia_inicial = int(input().split()[1])
hora_inicial, minuto_inicial, segundo_inicial = map(int, input().split(' : '))
dia_final = int(input().split()[1])
hora_final, minuto_final, segundo_final = map(int, input().split(' : '))

inicio = datetime.datetime(2024, 4, dia_inicial, hora_inicial, minuto_inicial, segundo_inicial)
fim = datetime.datetime(2024, 4, dia_final, hora_final, minuto_final, segundo_final)

duracao = fim - inicio

dias_totais = duracao.days
segundos_totais = duracao.seconds

horas_totais = segundos_totais // 3600
minutos_totais = (segundos_totais % 3600) // 60
segundos_totais = segundos_totais % 60

print(f'''{dias_totais} dia(s)
{horas_totais} hora(s)
{minutos_totais} minuto(s)
{segundos_totais} segundo(s)''')
