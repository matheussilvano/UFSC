dia_inicial, preco_inicial, varicao_diaria_do_preco, numero_de_dias = map(int, input().split(' '))

dia = dia_inicial
preco = preco_inicial

while dia < dia_inicial + numero_de_dias:
    if dia %2 == 0:
        preco += varicao_diaria_do_preco
    else:
        preco -= varicao_diaria_do_preco
    dia += 1
    
print(preco)
