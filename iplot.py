import numpy as np                     #Modulo para manejo de matrices
import matplotlib.pyplot as plt        #Modulo para graficar

from ipywidgets import interactive

#Definimos funciones periodicas
def coseno(x, A, T):
    return A * np.cos(x * 2 * np.pi / T)

def plot_coseno(A, T):
    t = np.linspace(0, 20, 1000)
    f = coseno(t, A, T)
    it = np.argmin(np.abs(t - T))
    max1 = np.argmax(f[:it])
    max2 = np.argmax(f[it:2*it])
    plt.plot(t, f, 'k-')
    plt.axvline(t[max1], color = 'red', ls = 'dashed')
    plt.axvline(t[it + max2], color = 'red', ls = 'dashed')
    plt.xlabel('Tiempo')
    plt.ylim(-20, 20)
    plt.show()

def cuadrado(x, A, L):
    y = x.copy()
    y[x % L <= L/2.0] = A 
    y[x % L > L/2.0] = -A 
    
    return y
    
def plot_cuadrado(A, T):
    x = np.linspace(0, 20, 1000)
    f = cuadrado(x, A, T)
    plt.plot(x, f, 'k-')
    plt.ylim(-20, 20)
    plt.axvline(T, color = 'red', ls = 'dashed')
    plt.axvline(2*T, color = 'red', ls = 'dashed')
    plt.xlabel('Tiempo')
    plt.show()

    
    
def icoseno():
    interactive_plot_seno = interactive(plot_coseno, A=(0, 20.), T=(0.1, 5, 0.1))
    output = interactive_plot_seno.children[-1]
    output.layout.height = '350px'
    return interactive_plot_seno

def icuadrado():    
    interactive_plot_cuadrado = interactive(plot_cuadrado, A=(0, 20.), T=(0.1, 10, 0.5))
    output = interactive_plot_cuadrado.children[-1]
    output.layout.height = '350px'
    return interactive_plot_cuadrado
