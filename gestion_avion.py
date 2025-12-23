from avion import Avion
from random import randint
from utilities import distance_avion, import_json_avion, import_json_data
from math import sqrt, degrees, atan2

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
            for data in dict_data.values():
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
    global L
    dict_avion = init_avion()
    for key in dict_avion.keys():
        for key__ in dict_avion.keys():
            if key__ == key:
                continue
            else:
                distance, delta_altitude = distance_avion(dict_avion[key], dict_avion[key__])
                if distance < 50 and delta_altitude <= 500:
                    dict_avion[key].etat['TCAS'] = True
                    dict_avion[key__].etat['TCAS'] = True
                elif distance <= 10 and delta_altitude <= 100:
                    L.remove(dict_avion[key].random_nb)
                    L.remove(dict_avion[key__].random_nb)
                    del(dict_avion[key])
                    del(dict_avion[key__])
        if dict_avion[key].consigne['landing'] == True:
            landing(dict_avion[key])
        else:
            dict_avion[key].exit_scope()
        try:
            dict_avion[key].heading_change()
            dict_avion[key].speed_change()
            dict_avion[key].vs_change()
            dict_avion[key].horizontal_move()
            dict_avion[key].vertical_move()
            dict_avion[key].distance_airport()
        except KeyError:
            continue
    return dict_avion

def landing(dict):
    airport_infos = dict.to
    distance = sqrt((dict.pos[0] - airport_infos[0]) ** 2 + (dict.pos[1] - airport_infos[1]) ** 2)
    dx = dict.pos[0] - airport_infos[0]
    dy = dict.pos[1] - airport_infos[1]
    angle = degrees(atan2(dy, dx))
    heading = round((270 + angle) % 360)
    if dict.alt > 3000 and distance > 2 and (abs((heading - dict.heading + 180) % 360 - 180) > 2):
        dict.speed = 0
        dict.consigne_change({'alt' : 3000, 'heading' : heading, 'speed' : 0, 'vs' : 3500, 'landing' : True})
    elif dict.alt > 3000 and distance > 2 and (abs((heading - dict.heading + 180) % 360 - 180) <= 2):
        dict.speed = dict.landing_speed
        dict.consigne_change({'alt': 3000, 'heading': heading, 'speed': dict.landing_speed, 'vs': 3500, 'landing': True})
    elif dict.alt > 3000 and distance <= 2:
        dict.speed = 0
        dict.pos = [airport_infos[0], airport_infos[1]]
        dict.consigne_change({'alt': 3000, 'heading': dict.heading + 5, 'speed': dict.landing_speed, 'vs': 3500, 'landing': True})
    elif dict.alt <= 3020 and dict.alt > 2980 and distance > 2:
        dict.alt = 3000
        dict.consigne_change({'alt': 3000, 'heading': heading, 'speed': dict.landing_speed, 'vs': None, 'landing': True})
    elif dict.alt <= 3020 and dict.alt > 2980 and distance <= 2 and dict.heading != (airport_infos[2] + 180) % 360:
        dict.pos = [airport_infos[0], airport_infos[1]]
        dict.speed = 0
        dict.alt = 3000
        dict.consigne_change({'alt': 3000, 'heading': (airport_infos[2] + 180) % 360, 'speed': 0, 'vs': None, 'landing': True})
    elif dict.alt <= 3020 and dict.alt > 2980 and distance <= 2 and dict.heading == (airport_infos[2] + 180) % 360:
        dict.speed = dict.landing_speed
        dict.consigne_change({'alt': 1500, 'heading': (airport_infos[2] + 180) % 360, 'speed': dict.landing_speed, 'vs': None, 'landing': True})
    elif dict.alt > 1520 and dict.alt < 3000:
        dict.speed = dict.landing_speed
        dict.consigne_change({'alt': 1500, 'heading': (airport_infos[2] + 180) % 360, 'speed': dict.landing_speed, 'vs': None, 'landing': True})
    elif dict.alt <= 1520 and dict.alt > 1480 and dict.heading != airport_infos[2]:
        dict.speed = 0
        dict.alt = 1500
        dict.consigne_change({'alt': 1500, 'heading': airport_infos[2], 'speed': 0, 'vs': None, 'landing': True})
    elif dict.alt <= 1500 and dict.heading == airport_infos[2]:
        dict.speed = dict.landing_speed
        dict.consigne_change({'alt': 0, 'heading': airport_infos[2], 'speed': dict.landing_speed, 'vs': None, 'landing': True})
    if dict.alt == 0:
        global dict_avion
        dict.etat['land ?'] = True

def check_avion():
    global dict_avion
    keys = []
    for key in dict_avion.keys():
        try:
            if dict_avion[key].etat['land ?'] == True:
                keys.append(key)
        except KeyError:
            continue
    for key in keys:
        try:
            L.remove(dict_avion[key].random_nb)
            del (dict_avion[key])
        except KeyError:
            continue
    return dict_avion

def clear_dict_avion():
    global dict_avion
    global L
    dict_avion = {}
    L =  []
