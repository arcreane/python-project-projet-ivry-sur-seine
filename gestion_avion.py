from avion import Avion
from fonction_json import import_json
from random import randint

FIR = "reims"
L = []
dict_avion = {}

while True:
    while len(dict_avion.keys()) <= 4:
        for i in range(5 + 1):
            if f'avion{i}' not in dict_avion.keys():
                n = randint(0, 25) not in L
                L.append(n)
                dict_cara = import_json(FIR, n)
                dict_avion[f'avion{i}'] = Avion(item for item in dict_cara.items())

    for key in dict_avion.keys():
        dict_avion[key].heading_change()
        dict_avion[key].speed_change()
        dict_avion[key].vs_change()
        dict_avion[key].horizontal_move()
        dict_avion[key].vertical_move()