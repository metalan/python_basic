# Author Vladimir SR
import random
"""
Python 1
10- Definir un histograma procedimiento() que tome una lista de números enteros
e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7])
debería imprimir lo siguiente:
****
*********
*******
"""


def procedimiento():
    max = random.randint(2, 5)
    historiograma = []
    for cont in range(1, max):
        historiograma.append(random.randint(2, 9))
    for cont in range(1, len(historiograma)):
        imprimir = ""
        for wr in range(1, historiograma[cont]):
            imprimir = imprimir + "*"
        print(imprimir)

"""
Python 2
Ejercicio 5
Construir un pequeño programa que convierta números binarios en enteros.
"""


def bin_a_int(numero=111111):
    largo = len(str(numero))
    total = 0
    for cont in range(0, largo):
        total += 2 ** cont
    print(total)

"""
Python 3
Ejercicio 1

Diseñar un sistema de puntos para el juego El reino del dragón:
La idea es la siguiente: mientras el jugador vaya ganando, ira acumulando puntos.
Ejemplo: Si el jugador entra en la primera cueva y gana el tesoro, se le acreditan 
100 puntos, entra en la segunda cueva y gana el tesoro, se le acreditan otros 100 
puntos. Si el jugador pierde, saldrá en pantalla el total de los puntos que realizo 
y la opción de empezar de nuevo.
"""


def puntuacion(puntos, ganado=True):
    if ganado:
        puntos += 100
    else:
        print(puntos)
        empezar_de_nuevo()
