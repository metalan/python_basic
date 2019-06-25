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

"""
Ejercicio 1
Determinar la cantidad de dígitos de un numero (1- 100000)
"""


def ej1():
    print(len(str(input("Escribe un número y te digo cuantos dígitos tiene:"))))


"""
Ejercicio 2 
Para un numero N menor de 100. Mostrar la suma de los cuadrados 
de los números que están separados entre si cuatro posiciones.
"""


def ej2(n):
    if n < 100:
        total = 0
        while n < 100:
            total += n**2
            n += 4

"""
Ejercicio 3
Imprimir 10 veces la serie de números de 1 a 10.
"""


def ej3():
    for cont in range(0, 10):
        for wr in range(1, 11):
            print(wr, "")

"""
Ejercicio 4
Para un número N imprimir su tabla de multiplicar.
"""


def ej4(n):
    for tabla in range(0, 11):
        print(n, "x", tabla, "= ", n * tabla)

"""
Ejercicio 5
Identificar si la suma de los dígitos de un numero es par o impar.
"""


def ej5(num1):
    total = 0
    for b in str(num1):
        total += int(b)
    if total % 2 == 0:
        print(num1, " es par")
    else:
        print(num1, " es impar")

"""
Ejercicio 6
Solicitar un número e imprimir los dígitos pares de este.
"""



"""
Ejercicio 7
Los números de las claves de dos cajas fuertes están mezcladas 
en un número entero llamado clave maestra. Determine ambas claves, 
la primera clave se construye con los dígitos impares de la clave 
maestra y la segunda con los pares. 
Ejemplo: Clave Maestra= 12345, clave1=135, clave2=24.
"""
