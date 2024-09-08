vitorias_c, empates_c, saldo_c, vitorias_f, empates_f, saldo_f = map(int, input().split(' '))
pontos_c = (vitorias_c * 3) + empates_c
pontos_f = (vitorias_f * 3) + empates_f
if pontos_c > pontos_f:
    print('C')
elif pontos_f > pontos_c:
    print('F')
else:
    if saldo_c > saldo_f:
        print('C')
    elif saldo_f > saldo_c:
        print('F')
    else:
        print('=')