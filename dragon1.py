# Julio, Sergio, Vicky
#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Reino del Dragon....
import random
import time

def introduccion():
    print("Estamos en una tierra llena de dragones. Delante de nuestro,")
    print("se ven dos cuevas. En una cueva, el dragon es amigable")
    print("y compartira el tesoro contigo. El otro dragon")
    print("es codicioso y hambriento, y te va a comer ni bien te vea.")
    print("")


def CambiarCueva():
    cueva = ""
    while cueva != "1" and cueva != "2":
        print("Ha que cueva quieres entrar? 1 o 2?")
        cueva = input()

    return cueva
