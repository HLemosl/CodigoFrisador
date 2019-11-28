#coding: UTF-8

import numpy as np
import cv2

caminhoDaImagem = raw_input()
diretorioImagem = raw_input()
imagem = cv2.imread(caminhoDaImagem)

#(1)Translação:

Translacao = np.hstack((imagem, imagem, imagem, imagem))
cv2.imwrite(diretorioImagem + "/" + "Translacao.png", Translacao)

#(2)Reflexão Horizontal:

ReflexaoH = cv2.flip(imagem, 0)
RHorizontal = np.vstack((imagem, ReflexaoH))
ReflexaoHorizontal = np.hstack((RHorizontal, RHorizontal, RHorizontal, RHorizontal))
cv2.imwrite(diretorioImagem + "/" + "Reflexão Horizontal.png", ReflexaoHorizontal)

#(3)Reflexao Vertical:

# 1 - vertical
# 0 - horizontal
# -1 - vertical e horizontal

ReflexaoV = cv2.flip(imagem, 1)
RVertical = np.vstack((imagem, ReflexaoV, imagem, ReflexaoV))
cv2.imwrite(diretorioImagem + "/" + "Reflexao Vertical.png", RVertical)

#(4)Reflexao Vertical + Horizontal:

ReflexaoVH = cv2.flip(imagem, -1)
RVerticalHorizontal = np.vstack((imagem, ReflexaoVH))
RVh = cv2.flip(RVerticalHorizontal, 1)
RVH = np.hstack((RVerticalHorizontal, RVh, RVerticalHorizontal, RVh))
cv2.imwrite(diretorioImagem + "/" + "Reflexao Verical e Horizontal.png", RVH)

#(5)Reflexao Deslizante + Vertical:

passo1 = cv2.flip(imagem, -1)
passo2 = np.vstack((imagem, passo1))
passo3 = cv2.flip(passo2, 1)
final = np.hstack((passo2, passo3, passo2, passo3))
cv2.imwrite(diretorioImagem + "/" +  "Reflexao Deslizante e Vertical.png", final)

#(6)Reflexao Horizontal + Translacao:

RHT1 = np.hstack((imagem, ReflexaoH, imagem, ReflexaoH))
cv2.imwrite(diretorioImagem + "/" + "Reflexao Horizontal e Translacao - Tipo 1.png", RHT1)

imagem2 = cv2.imread(caminhoDaImagem)
for y in range(0, imagem.shape[0]):
	for x in range(0, imagem.shape[1]):
		imagem[x,y] = (255, 255, 255)
RTH2 = np.vstack((imagem2, imagem))
passo1RTH2 = cv2.flip(RTH2, 0)
finalRTH2 = np.hstack((RTH2, passo1RTH2, RTH2, passo1RTH2))
cv2.imwrite(diretorioImagem + "/" + "Reflexao Horizontal e Translacao - Tipo 2.png", finalRTH2)

#(7)Rotação 180:

finalR = np.hstack((imagem2, passo1, imagem2, passo1))
cv2.imwrite(diretorioImagem + "/" + "Rotação 180.png", finalR)
