# Author Vladimir SR


def lists_methods():
    male_names = ["Alvaro", "Jacinto", "Miguel", "Edgardo", "David"]
    male_names.append("Jose")
    print(male_names)

    male_names.extend(["Jose", "Gerardo"])
    print(male_names)

    male_names.insert(0, "Ricky")
    print(male_names)

    male_names.pop()
    print(male_names)

    male_names.pop(3)
    print(male_names)

    male_names.remove("Jose")
    print(male_names)

    male_names.reverse()
    print(male_names)

    male_names.sort()
    print(male_names)

    male_names.sort(reverse=True)
    print(male_names)

    male_names = ["Alvaro", "Miguel", "Edgardo", "David", "Miguel"]
    male_names.count("Miguel")

    male_names = ("Alvaro", "Miguel", "Edgardo", "David", "Miguel")
    male_names.count("Miguel")

    male_names.index("Miguel")
    male_names.index("Miguel", 2, 5)

    tupla = (1, 2, 3, 4)
    tupla

    list(tupla)

    lista = [1, 2, 3, 4]
    lista

    tuple(lista)

    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6, 7, 8]
    list3 = list1 + list2

    list3

    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = (4, 6, 8, 10)
    tuple3 = (3, 5, 7, 9)
    tuple4 = tuple1 + tuple2 + tuple3

    tuple4

    max(tuple4)
    max(tuple1)
    min(tuple1)
    max(list3)
    min(list1)

    len(list3)
    len(list1)
    len(tuple2)


