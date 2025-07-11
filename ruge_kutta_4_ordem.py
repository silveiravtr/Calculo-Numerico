# -*- coding: utf-8 -*-
"""Untitled22.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qm8VZmjm9t8lvRfK0WQCfgUpdc4cGYj8
"""

'''
Nome: João Vítor Brito da Silveira

Método: Runge-Kutta de 4°Ordem

Resumo:O método de runge-kutta de 4°ordem é uma técnica para encontrar uma
aproximação da solução de uma equação diferencial, que descreve como uma
quantidade muda ao longo do tempo. Em resumo, o método RK4 calcula a solução de
uma equação diferencial de forma precisa ao usar várias estimativas
intermediárias e combiná-las para obter uma solução mais exata em
cada passo de tempo.
'''

#Importando funções matematicas
import numpy as np
import matplotlib.pyplot as plt

#Definindo a função f(x, y)=-2x^3 + 12x^2 - 20x + 8.5
def f(x, y):
    return -2*x**3+12*x**2-20*x+8.5

#Função que define a solução exata da equação diferencial, para fins de comparação
def solucao_exata(x):
    return -0.5*x**4+4*x**3-10*x**2+8.5*x+1

#Método de Runge-Kutta de 4ª Ordem
def runge_kutta_4(f, x0, y0, h, n):
    #Inicializando arrays para armazenar os resultados
    #x armazenará os valores de x, e y armazenará os valores de y
    x=np.zeros(n+1)
    y=np.zeros(n+1)

    #Definindo os valores iniciais de x e y (condições iniciais)
    x[0]=x0
    y[0]=y0

    #Loop para aplicar o método de Runge-Kutta em cada intervalo
    for i in range(n):

        # Calculando os incrementos k1, k2, k3, k4 com base nas inclinações da função
        k1=f(x[i], y[i])
        k2=f(x[i]+ 0.5*h, y[i]+0.5*k1*h)
        k3=f(x[i]+ 0.5*h, y[i]+0.5*k2*h)
        k4=f(x[i]+ h, y[i]+k3*h)

        #Atualizando o valor de y usando uma média ponderada dos k's
        y[i+1]=y[i]+(h/6)*(k1+2*k2+2*k3+k4)

        #Atualizando o valor de x para o próximo passo
        x[i+1]=x[i]+h

    #Retornando os arrays com os valores de x e y
    return x, y

#Definindo os parâmetros do problema
x0=0 #Ponto inicial de x
y0=1 #Condição inicial y(0) = 1
h=0.5 #Tamanho do passo h (intervalo entre cada cálculo)
n=int(4/h) #Número de passos para ir de x = 0 a x = 4

# Resolvendo o problema usando o método de Runge-Kutta de 4ª ordem (RK4)
x, y_rk4 = runge_kutta_4(f, x0, y0, h, n)

# Calculando a solução exata para os mesmos valores de x, para comparar com a solução numérica
y_exact = solucao_exata(x)

# Exibindo os resultados em forma de tabela, mostrando x, y_RK4, y_Exata e o erro
print("x\t   y_RK4\t y_Exata\t Erro")
for i in range(len(x)):
    erro = abs(y_exact[i] - y_rk4[i])  # Calculando o erro absoluto
    print(f"{x[i]:.1f}\t {y_rk4[i]:.6f}\t {y_exact[i]:.6f}\t {erro:.6f}")

# Plotando os resultados para comparação gráfica
plt.plot(x, y_rk4, label='RK4', marker='o')           # Solução numérica RK4
plt.plot(x, y_exact, label='Solução Exata', linestyle='--')  # Solução exata
plt.title('Comparação: RK4 vs Solução Exata')         # Título do gráfico
plt.xlabel('x')                                       # Rótulo do eixo x
plt.ylabel('y')                                       # Rótulo do eixo y
plt.grid(True)                                        # Adiciona uma grade ao gráfico
plt.legend()                                          # Adiciona uma legenda
plt.show()                                            # Exibe o gráfico