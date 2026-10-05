from PIL import Image, ImageDraw, ImageFont
import os


def criar_image_tabuada():
    LARGURA = 600
    ALTURA = 600
    COR_FUNDO = (245, 235, 220)
    COR_CABECALHO = (225,200, 175)
    COR_LINHA = (210,180, 140)
    COR_TEXT0 = (90, 60, 40)

    image = Image.new('RGB', (LARGURA, ALTURA), color=COR_FUNDO)
    desenho = ImageDraw.Draw(image)

    NUM_LINHAS = 11
    NUM_COLUNAS = 11

    passo_x = LARGURA / NUM_COLUNAS
    passo_y = ALTURA / NUM_LINHAS

    desenho.rectangle([0, 0, passo_x, ALTURA], fill = COR_CABECALHO) 
    desenho.rectangle([0, 0, passo_y, LARGURA], fill = COR_CABECALHO) 


   
    # DESENHAR AS LINHAS NA GRELHA
    for i in range(NUM_COLUNAS + 1):
        x =  i * passo_x
        desenho.line([(x, 0), (x, ALTURA)], fill=COR_LINHA, width=2)

    for j in range(NUM_LINHAS + 1):
        y =  j * passo_y
        desenho.line([(0, y), (LARGURA, y)], fill=COR_LINHA, width=2)

    try:
        fonte = ImageFont.load_default()
    except:
        fonte = None

    for i in range(1, 11):
        texto_x = str(i)
        desenho.text((i * passo_x + passo_x/3, passo_y/3), texto_x, fill=COR_TEXT0, font=fonte)

        texto_y = str(i)
        desenho.text((passo_x/3, i * passo_y + passo_y / 3), texto_y, fill=COR_TEXT0, font= fonte)


    desenho.text((passo_x/3, passo_y/3), 'x', fill=COR_TEXT0, font=fonte)

    for linha in range(1, 11):
        for coluna in range(1, 11):
            resultado = str(linha * coluna)
            pos_x = coluna * passo_x + passo_x / 3
            pos_y = linha * passo_y + passo_y / 3
            desenho.text((pos_x, pos_y), resultado, fill=COR_TEXT0, font=fonte)

    # Guardar iamgem final
    pasta_saida = "saida_imagens"
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    caminho_ficheiro = os.path.join(pasta_saida, "tabuada_base.png")
    image.save(caminho_ficheiro)
    print(f'Imagem guardada com sucesso em: {caminho_ficheiro}')


if __name__ == "__main__":
    criar_image_tabuada()