# Implemente um jogo onde o usuário deve adivinhar o número escolhido
# pelo computador (entre 0 e 10). O Usuário irá digitando valores até descobrir
# este valor. Quando o usuário “acertar”, uma mensagem avisa o final do jogo
# (que o número correto foi digitado) e o número de tentativas. 

numero = 3
while True:
    entrada_usuario = int(input('Digite um número entre 0 e 10: '))
    if entrada_usuario == numero:
        print('Você acertou!')
        break
    else:
        print(f'O número não é {entrada_usuario}, tente novamente.')
