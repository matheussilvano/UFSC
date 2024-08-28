tempo_gasto_viagem_em_h = int(input())
velocidade_media_em_km_h = int(input())
distancia_percorrida = tempo_gasto_viagem_em_h * velocidade_media_em_km_h
quantidade_de_litros_de_gasolina = distancia_percorrida / 12
print(f'{quantidade_de_litros_de_gasolina:.3f}')
