from math import sqrt
import json

def distance_avion(plane_1, plane_2):
    delta_altitude = abs(plane_1.altitude - plane_2.altitude)
    distance = sqrt((plane_1['pos'][0]-plane_2['pos'][0])**2 + (plane_1['pos'][1]-plane_2['pos'][1])**2)
    if distance < 50 and delta_altitude <= 1000:
        plane_1['etat']['TCAS'] = True
        plane_2['etat']['TCAS'] = True
    elif distance == 0 and delta_altitude == 0:
        plane_1.__del__()
        plane_2.__del__()


def import_json_data(FIR, num_ligne):
    filename = f'data{FIR}.json'
    f = open(filename, 'r')
    dicts = json.load(f)
    return dict

def import_json_avion(FIR, num_ligne):
    filename = f'avion{FIR}.json'
    f = open(filename, 'r')
    dicts = json.load(f)
    dict = dicts[num_ligne]
    return dict