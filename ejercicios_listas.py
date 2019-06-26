# Author Vladimir SR
import random
"""
Ejercicio 1
Escriba una función que tome una lista de números y devuelva la suma acumulada,
es decir, una nueva lista donde el primer elemento es el mismo, el segundo
elemento es la suma del primero con el segundo, el tercer elemento es la suma
del resultado anterior con el siguiente elemento y así sucesivamente. Por
ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].
"""


def con1():
    max = random.randint(2, 7)
    lista = []
    for cont in range(1, max):
        lista.append(random.randint(2, 9))
    resultado = []
    for cont in range(0, max -1):
        if cont == 0:
            resultado.append(lista[cont])
        else:
            resultado.append(lista[cont] + lista[cont - 1])
    return lista, resultado

"""
Ejercicio 2
Escribe una función llamada "elimina" que tome una lista y elimine el primer 
y último elemento de la lista y cree una nueva lista con los elementos que 
no fueron eliminados. Luego escribe una función que se llame "media" que tome 
una lista y devuelva una nueva lista que contenga todos los elementos de la 
lista anterior menos el primero y el último.
"""


"""
Ejercicio 3
Escribe una función "ordenada" que tome una lista como parámetro y devuelva 
True si la lista está ordenada en orden ascendente y devuelva False en caso 
contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada([b, a]) 
retorna False.
"""

