import csv
import statistics as st
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# X: numeros de desempregados de 2007 ate 2016 nos estados dos EUA
def leitura_csv_chave_valor(local):
    dados = {}
    with open(local) as arquivocsv:
        ler = csv.DictReader(arquivocsv, delimiter=";")
        for linha in ler:
            for chave, valor in linha.items():
                if chave not in dados:
                    dados[chave] = []

                #Para nao repetir valores de chave
                if (chave == 'estado'):
                    if (valor in dados['estado']):
                        break

                if (chave == 'quantidade'):
                    dados[chave].append(int(valor))
                else:
                    dados[chave].append(valor)

        return dados

def ler_csv():
    file = open("arquivo.csv", "r")
    reader = csv.reader(file)
    for line in reader:
        print(line[0], line[2])

def media_conjunto(conjunto):
    return st.mean(conjunto)

def mediana_conjunto(conjunto):
    return st.median(conjunto)

def moda_conjunto(conjunto):
    return stats.mode(conjunto)[0]

def desvio_padrao(conjunto):
    return st.pstdev(conjunto)

def is_outlier(points, thresh=3.5):
    if len(points.shape) == 1:
        points = points[:,None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh

#--------------------------------------------------------------------------------#
#                                   Inicio                                       #
#--------------------------------------------------------------------------------#

dados = leitura_csv_chave_valor("desempregados.csv")
print('***************************** 1 *****************************')
print("Tamanho: ", len(dados["estado"]))
print("Media: ", "%.2f" % media_conjunto(dados["quantidade"]))
print("Mediana: ", "%.2f" % mediana_conjunto(dados["quantidade"]))
print("Moda: ", "%.2f" % moda_conjunto(dados["quantidade"]))
print("Desvio padrao: ", "%.2f" % desvio_padrao(dados["quantidade"]))
# print("nome dos estados", dados["nome"])

plt.boxplot(dados["quantidade"])
plt.title('Boxplot da distribuicao das medias de pessoas desempregadas em {} estados dos EUA'.format(len(dados["estado"])))

plt.figure()
plt.boxplot(dados["quantidade"], 0, '')
plt.title('Boxplot da distribuicao das medias de pessoas desempregadas em {} estados dos EUA sem outliers'.format(len(dados["estado"])))

plt.figure()
plt.hist(dados["quantidade"], normed=True)
plt.title('Distribuicao das medias de pessoas desempregadas em {} estados dos EUA'.format(len(dados["estado"])))

x = np.array(dados["quantidade"])
filtrado = x[~is_outlier(x)]
plt.figure()
plt.hist(filtrado, normed=True)
plt.title('Distribuicao das medias de pessoas desempregadas em {} estados dos EUA sem outliers'.format(len(dados["estado"])))

plt.figure()
stats.probplot(dados["quantidade"], plot=plt)
plt.title('Normal probability plot para {} estados'.format(len(dados["estado"])))

plt.figure()
stats.probplot(filtrado, plot=plt)
plt.title('Normal probability plot para {} estados sem outliers'.format(len(dados["estado"])))
plt.show()
print('*************************************************************')

dados = leitura_csv_chave_valor("desempregados_subset.csv")
print('**************************** 2 ******************************')
print("Tamanho: ", len(dados["estado"]))
print("Media: ", "%.2f" % media_conjunto(dados["quantidade"]))
print("Mediana: ", "%.2f" % mediana_conjunto(dados["quantidade"]))
print("Moda: ", "%.2f" % moda_conjunto(dados["quantidade"]))
print("Desvio padrao: ", "%.2f" % desvio_padrao(dados["quantidade"]))
# print("nome dos estados", dados["nome"])

plt.boxplot(dados["quantidade"])
plt.title('Boxplot da distribuicao das medias de pessoas desempregadas em {} estados dos EUA'.format(len(dados["estado"])))

plt.figure()
plt.boxplot(dados["quantidade"], 0, '')
plt.title('Boxplot da distribuicao das medias de pessoas desempregadas em {} estados dos EUA sem outliers'.format(len(dados["estado"])))

plt.figure()
plt.hist(dados["quantidade"], normed=True)
plt.title('Distribuicao das medias de pessoas desempregadas em {} estados dos EUA'.format(len(dados["estado"])))

x = np.array(dados["quantidade"])
filtrado = x[~is_outlier(x)]
plt.figure()
plt.hist(filtrado, normed=True)
plt.title('Distribuicao das medias de pessoas desempregadas em {} estados dos EUA sem outliers'.format(len(dados["estado"])))

plt.figure()
stats.probplot(dados["quantidade"], plot=plt)
plt.title('Normal probability plot para {} estados'.format(len(dados["estado"])))

plt.figure()
stats.probplot(filtrado, plot=plt)
plt.title('Normal probability plot para {} estados sem outliers'.format(len(dados["estado"])))
plt.show()
print('*************************************************************')

dados = leitura_csv_chave_valor("desempregados_subset2.csv")
print('**************************** 3 ******************************')
print("Tamanho: ", len(dados["estado"]))
print("Media: ", "%.2f" % media_conjunto(dados["quantidade"]))
print("Mediana: ", "%.2f" % mediana_conjunto(dados["quantidade"]))
print("Moda: ", "%.2f" % moda_conjunto(dados["quantidade"]))
print("Desvio padrao: ", "%.2f" % desvio_padrao(dados["quantidade"]))
# print("nome dos estados", dados["nome"])

plt.boxplot(dados["quantidade"])
plt.title('Boxplot da distribuicao das medias de pessoas desempregadas em {} estados dos EUA'.format(len(dados["estado"])))

plt.figure()
plt.boxplot(dados["quantidade"], 0, '')
plt.title('Boxplot da distribuicao das medias de pessoas desempregadas em {} estados dos EUA sem outliers'.format(len(dados["estado"])))

plt.figure()
plt.hist(dados["quantidade"], normed=True)
plt.title('Distribuicao das medias de pessoas desempregadas em {} estados dos EUA'.format(len(dados["estado"])))

x = np.array(dados["quantidade"])
filtrado = x[~is_outlier(x)]
plt.figure()
plt.hist(filtrado, normed=True)
plt.title('Distribuicao das medias de pessoas desempregadas em {} estados dos EUA sem outliers'.format(len(dados["estado"])))

plt.figure()
stats.probplot(dados["quantidade"], plot=plt)
plt.title('Normal probability plot para {} estados'.format(len(dados["estado"])))

plt.figure()
stats.probplot(filtrado, plot=plt)
plt.title('Normal probability plot para {} estados sem outliers'.format(len(dados["estado"])))
plt.show()
print('*************************************************************')

dados = leitura_csv_chave_valor("desempregados_subset3.csv")
print('**************************** 4 ******************************')
print("Tamanho: ", len(dados["estado"]))
print("Media: ", "%.2f" % media_conjunto(dados["quantidade"]))
print("Mediana: ", "%.2f" % mediana_conjunto(dados["quantidade"]))
print("Moda: ", "%.2f" % moda_conjunto(dados["quantidade"]))
print("Desvio padrao: ", "%.2f" % desvio_padrao(dados["quantidade"]))
# print("nome dos estados", dados["nome"])

plt.boxplot(dados["quantidade"])
plt.title('Boxplot da distribuicao das medias de pessoas desempregadas em {} estados dos EUA'.format(len(dados["estado"])))

plt.figure()
plt.boxplot(dados["quantidade"], 0, '')
plt.title('Boxplot da distribuicao das medias de pessoas desempregadas em {} estados dos EUA sem outliers'.format(len(dados["estado"])))

plt.figure()
plt.hist(dados["quantidade"], normed=True)
plt.title('Distribuicao das medias de pessoas desempregadas em {} estados dos EUA'.format(len(dados["estado"])))

x = np.array(dados["quantidade"])
filtrado = x[~is_outlier(x)]
plt.figure()
plt.hist(filtrado, normed=True)
plt.title('Distribuicao das medias de pessoas desempregadas em {} estados dos EUA sem outliers'.format(len(dados["estado"])))

plt.figure()
stats.probplot(dados["quantidade"], plot=plt)
plt.title('Normal probability plot para {} estados'.format(len(dados["estado"])))

plt.figure()
stats.probplot(filtrado, plot=plt)
plt.title('Normal probability plot para {} estados sem outliers'.format(len(dados["estado"])))
plt.show()
print('*************************************************************')
