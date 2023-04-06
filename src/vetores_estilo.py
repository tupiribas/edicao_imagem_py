def vetor_titulo(msg='', simbolo=''):
    print(str(simbolo)*65)
    print(str(simbolo)*18, msg, str(simbolo)*18)
    print(str(simbolo)*65)


def vetor_escolha_caso(opcoes=[]):
    print('\nEscolha qual sua opção de transformação: ')
    for i, t in enumerate(opcoes):
        print(f'[{i+1}] -', t)
    escolha = int(input()) - 1
    return escolha
