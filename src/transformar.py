from tensorflow import io, image


def transformar_em_jpeg(caminho_img: str = '') -> bytes:
    """
    Transforma uma imagem em formato suportado pelo TensorFlow em um arquivo
    .jpeg.

    Args:
        caminho_img (str, opcional): O caminho completo do arquivo de imagem
        a ser transformado. O valor padrão é uma string vazia ("").

    Returns:
        bytes: O conteúdo do arquivo de imagem transformado em formato .jpeg.

    Raises:
        TypeError: Se o caminho do arquivo não for uma string.

    Example:
        >>> img_jpeg = transformar_em_jpeg('imagem.png')
    """
    if not isinstance(caminho_img, str):
        raise TypeError("O caminho do arquivo deve ser uma string.")
    img = io.read_file(filename=caminho_img)
    img = io.decode_jpeg(contents=img, channels=3)
    img = io.encode_jpeg(image=img)
    return img


def transformar_img_cinza(caminho_img: str = '') -> bytes:
    """
    Transforma uma imagem em escala de cinza e a retorna como bytes
    codificados em JPEG.

    Args:
        caminho_img (str, opcional): O caminho completo para a imagem a ser
        transformada. O valor padrão é uma string vazia ("").

    Returns:
        bytes: A imagem transformada em escala de cinza, codificada em formato
        JPEG.

    Raises:
        TypeError: Se o caminho da imagem não for uma string.

    Example:
        >>> img_codificada = transformar_img_cinza('C:/pasta/arquivo.jpg')
        >>> salvar_imagem(img_codificada, 'C:/pasta/novo/arquivo_cinza.jpeg')
    """
    if not isinstance(caminho_img, str):
        raise TypeError("O caminho da imagem deve ser uma string.")
    img = io.read_file(filename=caminho_img)
    img = io.decode_jpeg(contents=img, channels=3)
    img = image.rgb_to_grayscale(images=img)
    img = io.encode_jpeg(image=img)
    return img


def transformar_img_vertical(caminho_img: str = '') -> bytes:
    """
    Transforma uma imagem em sua versão verticalmente espelhada e
    rotacionada em 90 graus, e a retorna como bytes codificados em JPEG.

    Args:
        caminho_img (str, opcional): O caminho completo para a imagem a ser
        transformada. O valor padrão é uma string vazia ("").

    Returns:
        bytes: A imagem transformada em sua versão verticalmente espelhada e
        rotacionada em 90 graus, codificada em formato JPEG.

    Raises:
        TypeError: Se o caminho da imagem não for uma string.

    Example:
    >>> img_codificada = transformar_img_vertical('C:/pasta/arquivo.jpg')
    >>> salvar_imagem(img_codificada, 'C:/pasta/novo/arquivo_vertical.jpeg')
    """
    if not isinstance(caminho_img, str):
        raise TypeError("O caminho da imagem deve ser uma string.")
    img_transformada = io.read_file(filename=caminho_img)
    img_transformada = io.decode_jpeg(contents=img_transformada, channels=3)
    img_transformada = image.flip_left_right(img_transformada)
    img_transformada = image.rot90(img_transformada)
    img_transformada = io.encode_jpeg(image=img_transformada)
    return img_transformada


def salvar_imagem(img_codificada, novo_caminho_img=''):
    """
    Salva uma imagem codificada em formato JPEG no caminho especificado.

    Args:
        img_codificada (bytes): os bytes da imagem a ser salva.
        novo_caminho_img (str): o caminho completo do arquivo de imagem a ser
        salvo. O valor padrão é uma string vazia ("").

    Raises:
        TypeError: se os bytes da imagem não forem um objeto do tipo bytes ou
        o caminho da imagem não for uma string.

    Returns:
        None

    Example:
        >>> img_bytes = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01...'
        >>> salvar_imagem(img_bytes, 'C:/pasta/novo/arquivo.jpeg')
    """
    if not isinstance(novo_caminho_img, str):
        raise TypeError("O caminho da imagem deve ser uma string.")
    io.write_file(filename=novo_caminho_img, contents=img_codificada)
