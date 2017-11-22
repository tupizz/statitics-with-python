import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import math

def distribuicao_de_y(tamanho):
    valor_de_lambda = 1
    vetorY = []
    vetorX = []
    for i in range(tamanho+1):
        X = rnd.random()
        vetorX.append(X)
        Y = (-1/valor_de_lambda) * (math.log10(1 - X))
        vetorY.append(Y)
    plt.hist(vetorY, normed=True)
    plt.title('Distribuicao de Y com {} amostras'.format(tamanho))
    plt.show()

def exponencial(tamanho):
    plt.hist(np.random.exponential(1, tamanho), normed=True)
    plt.title('Distribuicao exponencial com {} amostras'.format(tamanho))
    plt.show()

def distribuicao_uniforme(tamanho):
    vetor = []
    for i in range(tamanho+1):
        vetor.append("%.2f" % rnd.random())
    plt.hist(vetor, normed=True)
    plt.title('Distribuicao Uniforme com {} amostras'.format(tamanho))
    plt.show()


distribuicao_uniforme(100000)
distribuicao_de_y(10000)
exponencial(10000)
