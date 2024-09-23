def verifica_colchao(comprimento, largura):
    tamanho_adequado = (1.90, 1.60)
    return (comprimento == tamanho_adequado[0]) and (largura == tamanho_adequado[1])

# Solicita as medidas do colchão
comprimento = float(input("Digite o comprimento do colchão em metros: "))
largura = float(input("Digite a largura do colchão em metros: "))

# Verifica se o colchão é adequado
if verifica_colchao(comprimento, largura):
    print("Parabéns pela compra! O colchão tem o tamanho adequado.")
else:
    print("Você deve procurar um outro colchão.")
