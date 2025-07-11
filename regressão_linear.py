# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fMFKEUD5txLD09ACrpWwSPtG8W97XSdC
"""

'''
Aluno: João Vítor Brito da Silveira

Método: Regressão linear por mínimos quadrados

Resumo: A Regressão Linear por Mínimos Quadrados é um método estatístico
utilizado para encontrar a reta que melhor se ajusta a um conjunto de dados.
Esse método é amplamente utilizado em análise de dados e modelagem preditiva.

Regressão Linear: É o processo de ajustar uma reta a um conjunto de pontos
de dados, onde a relação entre uma variável independente X e uma variável
dependente Y é modelada como uma linha reta.

Mínimos Quadrados: É a técnica utilizada para encontrar a reta de melhor ajuste.
O objetivo é minimizar a soma dos quadrados das diferenças (resíduos) entre
os valores observados e os valores preditos pela reta.
'''

#Importando funções matemáticas
import numpy as np

#Dados de entrada: listas com os valores da variável independente X e dependente Y
X=np.array([1, 2, 3, 4, 5, 6, 7])
Y=np.array([0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5])

#Número de observações (n)
n=len(X)

#Cálculo das somas necessárias
soma_X=np.sum(X)  #Soma de todos os valores de X
soma_Y=np.sum(Y)  #Soma de todos os valores de Y
soma_XY=np.sum(X*Y)  #Soma do produto dos pares correspondentes de X e Y
soma_X2=np.sum(X*X)  #Soma dos quadrados de cada valor de X

#Cálculo das médias de X e Y
media_X=soma_X/n  #Média de X
media_Y=soma_Y/n  #Média de Y

#Cálculo do coeficiente angular (a1) e do coeficiente linear (a0) da reta de regressão
a1=(n*soma_XY-soma_X*soma_Y)/(n*soma_X2-soma_X**2)  #Coeficiente angular
a0=(soma_Y-a1*soma_X)/n  #Coeficiente linear

#Cálculo dos valores ajustados de Y usando a equação da reta de regressão
Y_ajuste=a1*X+a0

#Cálculo do coeficiente de determinação (r^2) e do erro padrão da estimativa (syx)
St=np.sum((Y-media_Y)**2)  #Soma total dos quadrados em torno da média de Y
Sr=np.sum((Y-Y_ajuste)**2)  #Soma dos quadrados dos resíduos em torno da reta ajustada

r2=(St-Sr)/St  #Coeficiente de determinação, indica a qualidade do ajuste da reta
syx=np.sqrt(Sr/(n-2))  #Erro padrão da estimativa, mede a dispersão dos dados em torno da reta

#Exibição dos resultados
print(f"Coeficiente linear (a0): {a0}")
print(f"Coeficiente angular (a1): {a1}")
print(f"Coeficiente de determinação (r^2): {r2}")
print(f"Erro padrão da estimativa (syx): {syx}")

#Geração de um gráfico dos dados e da reta de regressão
import matplotlib.pyplot as plt

plt.scatter(X,Y,color='blue',label='Dados originais')  #Plotar os pontos de dados originais
plt.plot(X,Y_ajuste,color='red',label='Reta de Regressão')  #Plotar a reta ajustada
plt.xlabel('X')  #Rótulo do eixo X
plt.ylabel('Y')  #Rótulo do eixo Y
plt.legend()  #Adicionar legenda para identificar os dados e a reta
plt.title('Ajuste por Regressão Linear')  #Título do gráfico
plt.grid(True)  #Adicionar grade ao gráfico
plt.show()  #Mostrar o gráfico