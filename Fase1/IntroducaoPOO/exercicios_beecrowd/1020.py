entrada_idade_em_dias = int(input())
anos = entrada_idade_em_dias // 365
dias_restantes_ano = entrada_idade_em_dias % 365
meses = dias_restantes_ano // 30
dias = dias_restantes_ano % 30
print(f'''{anos} ano(s)
{meses} mes(es)
{dias} dia(s)''')
