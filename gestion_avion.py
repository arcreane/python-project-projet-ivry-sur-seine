from avion import Avion
from random import randint
from utilities import distance_avion, import_json_avion, import_json_data

dict_data = {}
L = []
dict_avion = {}

# creation du dico contenant les objets avion
def init_avion():
    global L
    global dict_data
    global dict_avion
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
                if data['name'] == dict_cara['to']:
                    to = [data['pos_x'], data['pos_y'], data['rwy_hdg']]
            dict_avion[dict_cara['callsign']] = Avion(dict_cara['callsign'],
                                  dict_cara['phonetic'],
                                  dict_cara['from_'],
                                  to,
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
                                  int(dict_cara['ldg_speed']),
                                  dict_cara['to'],
                                  n)
    return dict_avion

# gestion des mise à jours des paramètres avions et de la carte en fonction de l'échelle
def gestion_avion():
    global dict_data
    global dict_avion
    for key in dict_avion.keys():
        dict_avion[key].heading_change()
        dict_avion[key].speed_change()
        dict_avion[key].vs_change()
        dict_avion[key].horizontal_move()
        dict_avion[key].vertical_move()
        dict_avion[key].distance_airport()
        dict_avion[key].exit_scope(621, 451)
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
            dict_avion[key].landing()
            dict_avion.pop(key, None)

    return dict_avion