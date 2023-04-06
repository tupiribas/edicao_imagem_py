from tensorflow import io, image
# from os import path


def vetor_apresentacao():
    print('-'*50)


def imagem_cinza(caminho_img=''):
    img = io.read_file(filename=caminho_img)
    img = io.decode_jpeg(contents=img, channels=3, )
    img = image.rgb_to_grayscale(images=img)
    return img


def imagem_vertical(img_decod):
    img_transformada = image.flip_left_right(img_decod)
    img_transformada = image.rot90(img_transformada)
    return img_transformada


def salvar_imagem(img_decod, novo_caminho_img=''):
    img = io.encode_jpeg(img_decod)
    img = io.write_file(filename=novo_caminho_img,
                        contents=img)
    return img


# caminho_arquivo = './img/moon.jpeg'
# # Obter a extensão do arquivo
# extensao = path.splitext(caminho_arquivo)[1]
# # Transformar imagem em cinza
# img_transformada = imagem_cinza(caminho_arquivo)
# # Salvar imagem
# salvar_imagem(img_transformada, './img/novo/nova_foto_de_perfil.jpg')

vetor_apresentacao()
caminho_arquivo = ''
# while caminho_arquivo == ' ':
#     caminho_arquivo = input('Cole o caminho da imagem')
#     print(caminho_arquivo)
