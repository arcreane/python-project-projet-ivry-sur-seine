from avion import Avion
from random import randint
from utilities import distance_avion, import_json_avion, import_json_data
from math import sqrt, degrees, atan2

dict_data = {}
L = []
dict_avion = {}
nb_emergency = 0

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
                                  n,
                                  dict_cara['max'])
    return dict_avion

# gestion des mise à jours des paramètres avions et de la carte en fonction de l'échelle
def gestion_avion():
    global dict_data
    global dict_avion
    global L
    global nb_emergency
    dict_avion = init_avion()
    for key in dict_avion.keys():
        if dict_avion[key].sqwk != 7600 and dict_avion[key].sqwk != 7700 and nb_emergency <= 3:
            pb = randint(0, 500)
            if pb == 25:
                dict_avion[key].sqwk = 7600
                dict_avion[key].emergency = 'radio off'
                nb_emergency += 1
            elif pb == 50:
                dict_avion[key].sqwk = 7700
                nb_emergency += 1
                emergency = randint(0, 99)
                if emergency >= 0 and emergency <= 7:
                    dict_avion[key].emergency = 'engine failure'
                elif emergency >= 8 and emergency <= 20:
                    dict_avion[key].emergency = 'sick pax'
                elif emergency >= 21 and emergency <= 30:
                    dict_avion[key].emergency = 'electric failure'
                elif emergency >= 31 and emergency <= 40:
                    dict_avion[key].emergency = 'hydraulic failure'
                elif emergency >= 41 and emergency <= 56:
                    dict_avion[key].emergency = 'dangerous pax'
                elif emergency >= 57 and emergency <= 64:
                    dict_avion[key].emergency = 'engine fire'
                elif emergency >= 65 and emergency <= 75:
                    dict_avion[key].emergency = 'fire'
                elif emergency >= 76 and emergency <= 78:
                    dict_avion[key].emergency = 'fuel leak'
                elif emergency >= 79 and emergency <= 89:
                    dict_avion[key].emergency = 'pressure issue'
                else:
                    dict_avion[key].emergency = 'unknown issue'
        etat = False
        carbu = dict_avion[key].conso / 2
        if  carbu >= dict_avion[key].fuel:
            dict_avion[key].sqwk = 7700
            nb_emergency += 1
            if dict_avion[key].emergency != 'Normal':
                dict_avion[key].emergency = 'fuel'
            else:
                dict_avion[key].emergency += '\nfuel'
        if dict_avion[key].sqwk == 7600:
            dict_avion[key].etat['can land'] = True
            dict_avion[key].consigne_change({'landing' : True})
        elif dict_avion[key].sqwk == 7700:
            name = ['ALPHA', 'BRAVO', 'CHARLIE', 'DELTA', 'ECHO', 'FOXTROT']
            dict =  {}
            for data in dict_data.values():
                if data['name'] not in name:
                    dict_avion[key].to = [data['pos_x'], data['pos_y'], data['rwy_hdg']]
                    dict[data['name']] = dict_avion[key].distance_airport()
            airport = min(dict.values())
            for key_arpt, value in dict.items():
                if value == airport:
                    dict_avion[key].aprt_code = key_arpt
            if dict_avion[key].emergency == 'pressure issue':
                if dict_avion[key].alt > 10000 and dict_avion[key].consigne['alt'] > 10000:
                    dict_avion[key].consigne_change({'alt' : 10000, 'vs' : 6000})
            elif dict_avion[key].emergency == 'fuel leak':
                dict_avion[key].conso *= 1.5
            elif dict_avion[key].emergency == 'engine failure' or dict_avion[key].emergency == 'engine fire':
                if dict_avion[key].consigne['speed'] >= 200:
                    dict_avion[key].consigne_change({'speed' : 200})
                if dict_avion[key].consigne['alt'] >= 33000:
                    dict_avion[key].consigne_change({'alt' : 330000})
        for key__ in dict_avion.keys():
            if key__ == key:
                continue
            else:
                distance, delta_altitude = distance_avion(dict_avion[key], dict_avion[key__])
                if distance < 50 and delta_altitude <= 1000:
                    etat = True
                elif distance <= 10 and delta_altitude <= 100:
                    etat = True
                    dict_avion[key].etat['land ?'] = True
                    dict_avion[key__].etat['land ?'] = True
        dict_avion[key].etat['TCAS'] = etat
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
    global nb_emergency
    keys = []
    for key in dict_avion.keys():
        try:
            if dict_avion[key].etat['land ?'] == True:
                keys.append(key)
                if dict_avion[key].sqwk == 7600 or dict_avion[key].sqwk == 7700:
                    nb_emergency -= 1
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