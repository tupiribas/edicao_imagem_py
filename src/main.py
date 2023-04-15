from vetores_estilo import vetor_titulo, vetor_escolha_caso
from transformar import transformar_em_jpeg, salvar_imagem
from aplicacar_recurso import (
    aplicar_filtro_cinza_img, aplicar_mudar_img_vertical)
from tratamento_arquivo import caminho_padrao_salvo, verificar_transformar_jpeg


vetor_titulo('EDIÇÃO DE IMAGEM COM PYTHON', 'grande')
caminho_arquivo = str(input('Cole o caminho da imagem (.jpeg) aqui:\n'))

# Verificar o tipo do arquivo

if verificar_transformar_jpeg(caminho_arquivo, transformar=False):
    print('Trasnformando em JPEG...')
    img = transformar_em_jpeg(caminho_arquivo)
    caminho_arquivo = caminho_padrao_salvo(caminho_arquivo)
    salvar_imagem(img, caminho_arquivo)
    print('Arquivo transformado em JPEG e salvo com sucesso!\n')

vetor_titulo('Opção de Transformação', 'medio ', '*')
OPCOES = ['Filtro preto e Braco', 'Deixar na vertical']
escolha = vetor_escolha_caso(OPCOES)
if escolha == 0:
    aplicar_filtro_cinza_img(OPCOES[escolha], caminho_arquivo)
elif escolha == 1:
    aplicar_mudar_img_vertical(OPCOES[escolha], caminho_arquivo)
