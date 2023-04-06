from vetores_estilo import vetor_titulo, vetor_escolha_caso
from transformar_img import transformar_em_jpeg, salvar_imagem, imagem_cinza
from tratamento_arquivo import caminho_padrao_salvo


vetor_titulo('EDIÇÃO DE IMAGEM COM PYTHON', '-')
caminho_arquivo = str(input('Cole o caminho da imagem (.jpeg) aqui:\n'))

print('Trasnformando em JPEG...')
img = transformar_em_jpeg(caminho_arquivo)
caminho_arquivo = caminho_padrao_salvo(caminho_arquivo)
salvar_imagem(img, caminho_arquivo)
print('Arquivo transformado em JPEG e salvo com sucesso!')

print('Transformar a imagem em: ')
OPCOES = ['Preto e Braco']
escolha = vetor_escolha_caso(OPCOES)
if escolha == 0:
    print(f'Aplicando filtro {OPCOES[escolha]}...')
    img = imagem_cinza(caminho_arquivo)
    salvar_imagem(img, caminho_arquivo)
    print('Fitro aplicado com sucesso!')
