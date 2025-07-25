# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VzYU0flwcPXMFsUvNImAIc-_d66ahULt
"""

'''
Nome: João Vítor Brito da Silveira

Método: Polinômios interpoladores por diferenças dividida de Newton

Resumo: Polinômios interpoladores por diferenças divididas de Newton são uma
técnica utilizada para aproximar funções por polinômios, com base em um
conjunto de pontos de dados. Esse método é especialmente útil quando se precisa
construir um polinômio que passe exatamente por um conjunto dado de pontos e
deseja fazer isso de forma eficiente e numérica.

Polinômios Interpoladores: São polinômios construídos para passar exatamente
por um conjunto de pontos dados. A interpolação é o processo de encontrar
um polinômio que passa exatamente por todos os pontos fornecidos.

Diferenças Divididas: É uma forma de calcular os coeficientes do polinômio
interpolador. As diferenças divididas são utilizadas para construir o polinômio
de interpolação de Newton de forma eficiente
'''

#Importar funções matemáticas
import numpy as np
import matplotlib.pyplot as plt

#Dados fornecidos para interpolação
x=np.array([1, 4, 6, 5])  #Pontos x
y=np.array([0, 1.386294, 1.791759, 1.609438])  #Valores correspondentes f(x)

#Número de pontos menos 1 (n=grau do polinômio)
n=len(x)-1

#Inicializar a tabela de diferenças divididas
dif_div=np.zeros((n+1, n+1))
dif_div[:,0]=y  #A primeira coluna da tabela é simplesmente os valores de y

#Calcular as diferenças divididas
for j in range(1, n+1):  #Para cada ordem de diferença dividida
    for i in range(n-j+1):  #Para cada entrada na tabela de diferenças divididas
        dif_div[i,j]=(dif_div[i+1,j-1]-dif_div[i,j-1])/(x[i+j]-x[i])

#Função para calcular o valor do polinômio interpolador de Newton
def interpolacao_newton(z):
    termos_x=1
    y_int=dif_div[0,0]  #Começa com o termo constante
    for ordem in range(1, n+1):
        termos_x*=(z-x[ordem-1])  #Atualiza o termo x^(ordem)
        y_int+=dif_div[0,ordem]*termos_x  #Adiciona o termo interpolado
    return y_int

#Gerar valores para o gráfico
valores_x=np.linspace(min(x)-1,max(x)+1, 500)  #Gera uma faixa de valores x para plotagem
valores_y=np.array([interpolacao_newton(xi) for xi in valores_x])  #Calcula os valores y correspondentes

#Calcular o valor de ln(2) no ponto de interesse (z = 2) e o erro relativo percentual
z=2
y_int=interpolacao_newton(z)  #Estimativa de ln(2) usando o polinômio de Newton
ln2_verdadeiro=0.6931472  #Valor verdadeiro de ln(2)
erro_relativo=abs((y_int-ln2_verdadeiro)/ln2_verdadeiro)*100  #Calcula o erro relativo percentual

#Plotar os dados
plt.figure(figsize=(10, 6))  #Cria uma nova figura com tamanho especificado
plt.plot(valores_x, valores_y, label='Curva Interpolada', color='blue')  #Plota a curva interpolada
plt.scatter(x, y, color='red', zorder=5, label='Dados Originais')  #Plota os pontos originais
plt.xlabel('x')  #Rótulo do eixo x
plt.ylabel('f(x)')  #Rótulo do eixo y
plt.title('Polinômio Interpolador de Newton')  #Título do gráfico
plt.legend()  #Adiciona uma legenda
plt.grid(True)  #Adiciona uma grade ao gráfico
plt.show()  #Exibe o gráfico

#Exibir resultados
print(f"Estimativa de ln(2) usando o polinômio interpolador de Newton: {y_int:.6f}")
print(f"Erro relativo percentual: {erro_relativo:.6f}%")