from tensorflow import io, image


def transformar_em_jpeg(caminho_img=''):
    img = io.read_file(filename=caminho_img)
    img = io.decode_jpeg(contents=img, channels=3)
    img = io.encode_jpeg(image=img)
    return img


def imagem_cinza(caminho_img=''):
    img = io.read_file(filename=caminho_img)
    img = io.decode_jpeg(contents=img, channels=3)
    img = image.rgb_to_grayscale(images=img)
    img = io.encode_jpeg(image=img)
    return img


def imagem_vertical(caminho_img=''):
    img_transformada = io.read_file(filename=caminho_img)
    img_transformada = io.decode_jpeg(contents=img_transformada, channels=3)
    img_transformada = image.flip_left_right(img_transformada)
    img_transformada = image.rot90(img_transformada)
    img_transformada = io.encode_jpeg(image=img_transformada)
    return img_transformada


def salvar_imagem(img_codificada, novo_caminho_img=''):
    io.write_file(filename=novo_caminho_img, contents=img_codificada)
