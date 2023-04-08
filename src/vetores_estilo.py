def vetor_titulo(msg: str, tamanho: str, simbolo='-'):
    if tamanho.lower()[0] == 'g':
        print(str(simbolo)*18+str(simbolo)*(len(msg)+2)+str(simbolo)*18)
        print(str(simbolo)*18, msg, str(simbolo)*18)
        print(str(simbolo)*18+str(simbolo)*(len(msg)+2)+str(simbolo)*18)
    elif tamanho.lower()[0] == 'm':
        print(str(simbolo)*8+str(simbolo)*(len(msg)+2)+str(simbolo)*8)
        print(str(simbolo)*8, msg, str(simbolo)*8)
        print(str(simbolo)*8+str(simbolo)*(len(msg)+2)+str(simbolo)*8)
    elif tamanho.lower()[0] == 'p':
        print(str(simbolo)*1+str(simbolo)*(len(msg)+2)+str(simbolo)*1)
        print(str(simbolo)*1, msg, str(simbolo)*1)
        print(str(simbolo)*1+str(simbolo)*(len(msg)+2)+str(simbolo)*1)
    else:
        print(str(simbolo)*4, msg, str(simbolo)*1)


def vetor_escolha_caso(opcoes=[]):
    print('Escolha qual sua opção de transformação: ')
    for i, t in enumerate(opcoes):
        print(f'[{i+1}] -', t)
    escolha = int(input('Escolha: ')) - 1
    return escolha
