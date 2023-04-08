from transformar import (
    salvar_imagem, transformar_img_cinza, transformar_img_vertical)


def aplicar_filtro_cinza_img(opcao: list, caminho_arquivo: str):
    print(f'Aplicando filtro {str(opcao).lower()}...')
    img = transformar_img_cinza(caminho_arquivo)
    salvar_imagem(img, caminho_arquivo)
    print(f'Fitro aplicado com sucesso! \nLocal do arquivo: {caminho_arquivo}')


def aplicar_mudar_img_vertical(opcao: list, caminho_arquivo: str):
    print(f'Aplicando transformação: {str(opcao).lower()}...')
    img = transformar_img_vertical(caminho_arquivo)
    salvar_imagem(img, caminho_arquivo)
    print(
        f'Transformação: {opcao}, aplicado com sucesso!', end='\n')
    print(f'Local do arquivo: {caminho_arquivo}')
