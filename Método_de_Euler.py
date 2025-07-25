# -*- coding: utf-8 -*-
"""Untitled20.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13pn-1zgCcc4eOR6VRqOsH5ZUTudrJ38V
"""

''''
Nome: João Vítor Brito da Silveira

Método: Método de Euler

Resumo: O método de Euler é uma técnica numérica fundamental para a resolução de
EDOs, amplamente utilizado. Ele oferece uma maneira de aproximar soluções de
EDOs que são difíceis ou impossíveis de resolver analiticamente.

É um método de primeira ordem, o que significa que o erro global é
proporcional a h. Para problemas mais complexos ou onde alta precisão é
necessária, métodos mais avançados, como o método de Euler modificado ou
o método de Runge-Kutta, são preferíveis.
'''

#Importando funções matemáticas
import numpy as np
import matplotlib.pyplot as plt

#Definição da função f(x,y) conforme a equação diferencial dada
def f(x,y):
    return -2*x**3+12*x**2-20*x+8.5

#Condição inicial: valores iniciais de x e y
x0=0 #x inicial
y0=1 #y inicial (y(x0)=1)

#Definição do intervalo e tamanho do passo
a=0 #Limite inferior do intervalo
b=4 #Limite superior do intervalo
h=0.5 #Tamanho do passo

#Cálculo do número de subintervalos
N=int((b-a)/h)

#Criação dos vetores para armazenar os valores de x e y
x=np.linspace(a,b,N+1) #Gera os valores de x entre a e b com N+1 pontos
y=np.zeros(N+1) #Inicializa o vetor y com zeros

#Atribui o valor inicial de y
y[0]=y0  #y no ponto inicial é igual a y0

#Método de Euler
for i in range(N):
    y[i+1]=y[i]+h*f(x[i],y[i]) #Calcula o próximo valor de y

#Solução verdadeira
y_verdadeiro=-0.5*x**4+4*x**3-10*x**2+8.5*x+1

#Cálculo do erro relativo percentual verdadeiro
erro_relativo_percentual=np.abs((y_verdadeiro-y)/y_verdadeiro)*100

#Exibição dos resultados
print("x\t\t y (Método de Euler)\t y (Solução verdadeira)\t Erro relativo (%)")
for i in range(N+1):
    print(f"{x[i]:.2f}\t {y[i]:.5f}\t\t {y_verdadeiro[i]:.5f}\t\t {erro_relativo_percentual[i]:.2f}")

#Plotagem das soluções
plt.plot(x,y,'bo-',label='Método de Euler') #Solução aproximada com pontos azuis
plt.plot(x,y_verdadeiro,'r-',label='Solução verdadeira') #Solução verdadeira com linha vermelha
plt.xlabel('x') #Título do eixo x
plt.ylabel('y') #Título do eixo y
plt.legend() #Exibe a legenda no gráfico
plt.grid(True) #Ativa o grid no gráfico
plt.title('Método de Euler vs Solução verdadeira') #Título do gráfico
plt.show() #Mostra o gráfico