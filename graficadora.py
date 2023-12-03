from matplotlib import pyplot
import numpy as np


def mostrar_raiz(fx,raiz,metodo):
   # Valores del eje X que toma el gráfico.
   # valor inicia / valor final / #datos en ese intervalo
   espacio = np.linspace(-10, 10, 1100)
   y = fx(espacio)
   # Graficar cada punto (x,y).
   pyplot.plot(espacio, y)
   # Establecer el color de los ejes.
   pyplot.axhline(0, color="black")
   pyplot.axvline(0, color="black")
   # Limitar los valores de los ejes.
   pyplot.xlim(-10, 10)
   pyplot.ylim(-10, 10)
   # marcar el punto que queremos / mostrar con leyenda
   pyplot.plot(raiz[0], raiz[1], marker="o", markersize=5, markeredgecolor="red", markerfacecolor="red",label="Raiz: " + str(raiz))
   # mostrar significado del punto
   pyplot.legend()
   # Titulo del grafico
   pyplot.title('Metodo de la '+ metodo, size=14)
   # Mostrarlo.
   pyplot.show()