from os import path
from typing import Union


def caminho_padrao_salvo(caminho_arquivo: str = '') -> str:
    """
    Retorna o caminho padrão para o arquivo salvo com nome modificado.

    Args:
        caminho_arquivo (str, opcional): O caminho completo do arquivo
        original. O valor padrão é uma string vazia ("").

    Returns:
        str: O caminho completo para o arquivo salvo com o nome modificado.

    Raises:
        TypeError: Se o caminho do arquivo não for uma string.

    Example:
        >>> caminho_padrao_salvo('C:/pasta/arquivo.jpg')
        'C:/pasta/novo/arquivo.jpeg'
    """
    if not isinstance(caminho_arquivo, str):
        return TypeError("O caminho do arquivo deve ser uma string.")
    return str(path.dirname(caminho_arquivo) +
               '\\novo\\'+path.
               basename(str(verificar_transformar_jpeg(caminho_arquivo,
                                                       transformar=True))))


def verificar_transformar_jpeg(caminho_arquivo: str = '',
                               transformar: bool = False) -> Union[str, bool]:
    """
    Verifica se o arquivo especificado pelo caminho_arquivo é um arquivo .jpeg
    e, se necessário, o transforma.

    Args:
        caminho_arquivo (str): O caminho completo do arquivo a ser verificado
        e transformado, se necessário.
        transformar (bool, opcional): Um valor booleano que indica se o
        arquivo deve ser transformado. O valor padrão é False.

    Returns:
        Union[str, bool]: Se o parâmetro transformar é False e o arquivo não
        tem a extensão .jpeg, retorna True. Se o parâmetro transformar é True
        e o arquivo não tem a extensão .jpeg, retorna o caminho completo do
        arquivo com a extensão .jpeg adicionada. Se o arquivo já tem a extensão
        .jpeg, retorna o caminho completo do arquivo.

    Raises:
        TypeError: Se o caminho do arquivo não for uma string.

    Example:
        >>> verificar_transformar_jpeg('C:/pasta/arquivo.png')
        True
        >>> verificar_transformar_jpeg('C:/pasta/arquivo.png', True)
        'C:/pasta/arquivo.jpeg'
        >>> verificar_transformar_jpeg('C:/pasta/arquivo.jpeg')
        'C:/pasta/arquivo.jpeg'
    """
    if not isinstance(caminho_arquivo, str):
        return TypeError("O caminho do arquivo deve ser uma string.")
    if caminho_arquivo.split('.')[1] != 'jpeg' and transformar:
        return caminho_arquivo.split('.')[0] + '.jpeg'
    elif caminho_arquivo.split('.')[1] != 'jpeg' and not transformar:
        return True
    else:
        return caminho_arquivo
