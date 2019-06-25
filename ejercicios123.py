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
# Python 2
# Ejercicio 5
# Construir un pequeño programa que convierta números binarios en enteros.
"""

def bin_a_int(numero):
    largo = len(numero)
    total = 0

    for cont in range(0, largo):
        total +=