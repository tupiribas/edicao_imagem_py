from os import path


def caminho_padrao_salvo(caminho_arquivo=''):
    return str(path.dirname(caminho_arquivo) +
               '/novo/'+path.basename(caminho_arquivo))
