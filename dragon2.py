# Authors Vladi, Ana, Sara
from dragon1 import *
import time
import random

def cheqcueva(CambiarCueva):
    print("Te acercas a la Cueva...")
    time.sleep(2)
    print("Esta oscuro y tenebroso...")
    time.sleep(2)
    print("Un gran dragon salta delante tuyo, abre su boca y...")
    print("")
    time.sleep(2)

    FriendlyCueva = random.randint(1, 2)

    if CambiarCueva == str(FriendlyCueva):
        print("Te entrega el tesoro...")
    else:
        print("El dragon te come de un bocado....")


def empezar_de_nuevo():
    EmpezarNuevo = ("si")

    while EmpezarNuevo == ("s") or EmpezarNuevo == ("si"):
        introduccion()
        NumCaverna = CambiarCueva()
        cheqcueva(NumCaverna)
        print("Quieres jugar de nuevo? (si o no)")
        EmpezarNuevo = input()
