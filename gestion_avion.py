from avion import Avion
from random import randint
from utilities import distance_avion, import_json_avion, import_json_data

dict_data = {}
L = []

# creation du dico contenant les objets avion
def init_avion(dict_avion):
    global L
    global dict_data
    dict_data = import_json_data()
    while len(dict_avion.keys()) <= 5:
            n = randint(0, 19)
            while n in L:
                n = randint(0, 19)
            L.append(n)
            dict_cara = import_json_avion(n)
            for data in dict_data:
                if data['name'] ==  dict_cara['pos']:
                    pos = [data['pos_x'], data['pos_y']]
            dict_avion[n] = Avion(dict_cara['callsign'],
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
                                  pos,
                                  int(dict_cara['heading']),
                                  int(dict_cara['speed']),
                                  int(dict_cara['vs']),
                                  float(dict_cara['conso']),
                                  int(dict_cara['alt']),
                                  int(dict_cara['ldg_speed']))
    return dict_avion

# gestion des mise à jours des paramètres avions et de la carte en fonction de l'échelle
def gestion_avion(dict_avion ,scale_x, scale_y):
    global dict_data
    for key in dict_avion.keys():
        dict_avion[key].heading_change()
        dict_avion[key].speed_change()
        dict_avion[key].vs_change()
        dict_avion[key].horizontal_move(scale_x, scale_y)
        dict_avion[key].vertical_move()
        dict_avion[key].distance_airport(dict_data[dict_avion[key]['to']])
        dict_avion[key].exit_scope(621 * scale_x, 431 * scale_y)
        for key__ in dict_avion.keys():
            if key__ == key:
                continue
            else:
                distance, delta_altitude = distance_avion(dict_avion[key], dict_avion[key__])
                if distance < 50 and delta_altitude <= 1000:
                    dict_avion[key].etat['TCAS'] = True
                    dict_avion[key__].etat['TCAS'] = True
                elif distance == 0 and delta_altitude == 0:
                    dict_avion[key].__del__()
                    dict_avion[key__].__del__()
                    dict_avion.pop(key, None)
                    dict_avion.pop(key__, None)
        if dict_avion[key].consigne['landing'] == True:
            dict_avion[key].landing(dict_data[dict_avion[key]['to']])
            dict_avion.pop(key, None)

    for key,value in dict_data.items():
        dict_data[key][0] = value[0] * scale_x
        dict_data[key][1] = value[1] * scale_y

    return dict_avion