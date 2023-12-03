# vim: set fileencoding=utf-8
import argparse
from graficadora import *
from prettytable import PrettyTable

class Biseccion:

    def __init__(
        self,
        funcion: str,
        raiz=float,
        xn=float,
        xp=float,
    ) -> None:
       self.funcion = lambda x: eval(funcion)
       self.raiz = raiz
       self.xn = xn
       self.xp = xp
       self.precision = 1


    def inicio(self):
        # en caso de tener todas las x el programa no las busca
        if((self.xn is None) or (self.xp is None)):
         self.encontrar_Iniciales()
        self.generar_tabla()

    def encontrar_Iniciales(self):
        # la logica aqui es que siempre antes y despues 
        # de la raiz habra un valor diferente aunque 
        # puede haber tanto xp y xn por lado por lo que
        # depende de nuestra precision especificada
        self.conseguir_x(int(self.raiz+self.precision))
        self.conseguir_x(int(self.raiz-self.precision))

        
    def conseguir_x(self,num):
          val = self.funcion(num)
          #en caso de que ya tengamos x especificadas no se sobreescribiran
          if(val>0 and self.xp is None):
            self.xp = num
          if(val<0 and self.xn is None):
            self.xn = num


    def generar_tabla(self):
        #pasamos nuestros valores globales
        #para que no sea mucho texto
        xp = self.xp
        xn = self.xn
        fx = self.funcion
        # Inicio de nuestar tabla
        tabla = PrettyTable(["Iteracón","X", "f(x)"])
        tabla.add_row(["",str(xp)+" xp",fx(xp)])
        tabla.add_row(["",str(xn)+" xn",fx(xn)])
        xe = 0
        i = 1
        signo = ""
        val_fun = 0
        #si acertamos la raiz termina el bucle
        while(xe!=self.raiz):
          # en caso de no acertar con raiz especifica, terminara cuando se repita el valor x
          if(xe == round(xn + ((xp-xn)/2), 6)):
              break
         
          xe = round(xn + ((xp-xn)/2), 6)
          val_fun = round(fx(xe), 6)

          # Elige el nuevo valor de xn,xp en base al resultado de la funcion
          if(val_fun < 0):
             xn = xe
             signo = " xn"
          else:
             xp = xe
             signo = " xp"

          # agregamos una fila de nuestra tabla
          tabla.add_row([i,str(xe)+signo, val_fun])
        
          i+=1
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
        '--xp',
        dest='xp',
        action='store',
        type=float,
        help='X positiva',
    )
    parser.add_argument(
        '--xn',
        dest='xn',
        action='store',
        type=float,
        help='X negativa',
    )
    #leemos los argumentos que hemos creado
    args = parser.parse_args()
    #instanciacion de nuestro objeto
    metodo = Biseccion(args.funcion,args.raiz,args.xn,args.xp)
    metodo.inicio()