from avion import Avion
from random import randint
from utilities import distance_avion, import_json_avion, import_json_data
from time import sleep

FIR = "reims"
L = []
dict_avion = {}
dict_data = import_json_data(FIR)
new_size_x = 621
new_size_y = 431

while True:
    while len(dict_avion.keys()) <= 4:
        for i in range(5 + 1):
            if i not in dict_avion.keys():
                n = randint(0, 6)
                while n in L:
                    n = randint(0, 6)
                L.append(n)
                dict_cara = import_json_avion(FIR, n)
                dict_avion[i] = Avion(dict_cara['callsign'],
                                                dict_cara['phonetic'],
                                                dict_cara['from_'],
                                                dict_cara['to'],
                                                dict_cara['type_'],
                                                dict_cara['immat'],
                                                dict_cara['turb'],
                                                dict_cara['pax'],
                                                dict_cara['final_level'],
                                                dict_cara['sqwk'],
                                                float(dict_cara['fuel']),
                                                dict_data[dict_cara['pos']],
                                                int(dict_cara['heading']),
                                                int(dict_cara['speed']),
                                                int(dict_cara['vs']),
                                                float(dict_cara['conso']),
                                                int(dict_cara['alt']))

    scale_x = new_size_x / 621
    scale_y = new_size_y / 431
    for key in dict_avion.keys():
        dict_avion[key].heading_change()
        dict_avion[key].speed_change()
        dict_avion[key].vs_change()
        dict_avion[key].horizontal_move(scale_x, scale_y)
        dict_avion[key].vertical_move()
        dict_avion[key].distance_aiport(dict_data[dict_cara['to']])
        dict_avion[key].exit_scope(new_size_x, new_size_y)
        for key__ in dict_avion.keys():
            if key__ == key:
                continue
            else:
                distance_avion(dict_avion[key], dict_avion[key__])
        if dict_avion[key].consigne['landing'] == True:
            dict_avion[key].landing(dict_data[dict_cara['to']])

    for key,value in dict_data.items():
        dict_data[key][0] = value[0] * scale_x
        dict_data[key][1] = value[1] * scale_y

    sleep(1)