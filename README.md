## metodos_numericos
Repositorio con scripts que simulan las iteraciones de algunos metodos numéricos, dando como resultado su tabla y su grafica

## Instala las librerias requeridas

```
python -m pip install -r requirements.txt
```

## Uso

Se muestran todos lo parametros que podemos pasar, solo --funcion y --raiz son requeridos
Ejemplo para entender como escribir funciones:
```
x**2 + 5*x - 8  es lo mismo que x^2 + 5x - 8
```

#biseccion.py

```
python biseccion.py --funcion "x**4 + 3*x**3 -x**2 -5*x -2" --raiz 1.342923 --xp 2 --xn 0
```

#falsapos.py

```
python falsapos.py --funcion "x**4 - 3*x**3 +x**2 -5*x +2" --raiz 3.126259 --xp 4 --xn 2
```

#secante.py

```
python secante.py --funcion "x**3-3*x**2+5*x+2" --raiz -0.328268 --x -1 --x 0
```