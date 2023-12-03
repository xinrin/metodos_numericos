# vim: set fileencoding=utf-8
import argparse
from graficadora import *
from prettytable import PrettyTable

class Secante:

    def __init__(
        self,
        funcion: str,
        raiz=float,
        x=float,
        x1=float,
    ) -> None:
       self.funcion = lambda x: eval(funcion)
       self.raiz = raiz
       self.x = x
       self.x1 = x1
       self.precision = 1


    def inicio(self):
        # en caso de tener todas las x el programa no las busca
        if((self.x is None) or (self.x1 is None)):
         self.encontrar_Iniciales()
        self.generar_tabla()

    def encontrar_Iniciales(self):
        # la logica aqui es que siempre antes y despues 
        # de la raiz habra un valor diferente 
        # aqui se deben tomar en orden
        self.x = int(self.raiz-self.precision)
        self.x1 = int(self.raiz+self.precision)

    def generar_tabla(self):
        #pasamos nuestros valores globales
        #para que no sea mucho texto
        x = self.x
        x1 = self.x1
        fx = self.funcion
        
        # Inicio de nuestar tabla
        tabla = PrettyTable(["Iteracón","X", "f(x)"])
        tabla.add_row(["",x,fx(x)])
        tabla.add_row(["",x1,fx(x1)])
        #inicio de valores de soporte
        xe = 0
        i = 1
        val_fun = 0
        #si acertamos la raiz termina el bucle
        while(xe!=self.raiz):
          # en caso de no acertar con raiz especifica, terminara cuando se repita el valor x1
          if(xe == round(x1-(((x1-x)*fx(x1))/(fx(x1)-fx(x))),6)):
              break
         
          xe = round(x1-(((x1-x)*fx(x1))/(fx(x1)-fx(x))),6)
          val_fun = round(fx(xe),6)


          # agregamos una fila de nuestra tabla
          tabla.add_row([i,xe, val_fun])
          x = x1
          x1 = xe
        
          i+=1
        #mostramos nuestra tabla  
        print(tabla)
        #Mostramos la recta
        mostrar_raiz(fx,(xe,int(fx(xe))),"bisección")

            
if __name__ == "__main__":

    descripcion = "Script para conseguir la raiz de una funcion con el metodo de la biseccion"
    parser = argparse.ArgumentParser(description=descripcion)
    parser.add_argument(
        '--funcion',
        dest='funcion',
        action='store',
        type=str,
        required=True,
        help='Funcion deseada',
    )
    parser.add_argument(
        '--raiz',
        dest='raiz',
        action='store',
        type=float,
        required=True,
        help='Raiz o valor al que se busca llegar',
    )
    parser.add_argument(
        '--x',
        dest='x',
        action='store',
        type=float,
        help='Primera x',
    )
    parser.add_argument(
        '--x1',
        dest='x1',
        action='store',
        type=float,
        help='X + 1',
    )
    #leemos los argumentos que hemos creado
    args = parser.parse_args()
    #instanciacion de nuestro objeto
    metodo = Secante(args.funcion,args.raiz,args.x,args.x1)
    metodo.inicio()