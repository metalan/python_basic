# Author Vladimir SR


def dictionaries():
    diccionario = {"color": "violeta", "talle": "XS", "precio": 174.25}
    print(diccionario)
    diccionario.clear()
    print(diccionario)

    diccionario = {"color": "violeta", "talle": "XS", "precio": 174.25}
    remera = diccionario.copy()

    diccionario
    remera

    diccionario.clear()

    diccionario
    remera

    musculosa = remera

    remera
    musculosa

    remera.clear()

    remera
    musculosa

    secuencia = ["color", "talle", "marca"]
    diccionario1 = dict.fromkeys(secuencia)
    diccionario1

    diccionario2 = dict.fromkeys(secuencia, 'valor x defecto')
    diccionario2

    diccionario1 = {"color": "verde", "precio": 45}
    diccionario2 = {"talle": "M", "marca": "Lacoste"}
    diccionario1.update(diccionario2)
    diccionario1

    remera = {"color": "rosa", "marca": "Zara"}
    clave = remera.setdefault("talle", "U")
    clave

    remera

    remera2 = remera.copy()
    remera2

    clave = remera2.setdefault("estampado")
    clave
    remera2

    clave = remera2.setdefault("marca", "Lacoste")
    clave

    remera2

    remera.get("color")

    remera.get("stock")
    remera.get("stock", "sin stock")

    existe = remera.keys("precio")
    existe

    # existe = remera.keys("color")
    existe = "color" in remera
    existe

    diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
    for clave, valor in diccionario.items():
        print("El valor de la clave ", clave, " es ", valor)

    diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
    claves = diccionario.keys()
    claves

    diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
    valores = diccionario.values()
    valores

    diccionario = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
    len(diccionario)
