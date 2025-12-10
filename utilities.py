from math import sqrt
import json

def distance_avion(plane_1, plane_2):
    delta_altitude = abs(plane_1.altitude - plane_2.altitude)
    distance = sqrt((plane_1['pos'][0]-plane_2['pos'][0])**2 + (plane_1['pos'][1]-plane_2['pos'][1])**2)
    return distance, delta_altitude


def import_json_data(FIR, num_ligne):
    filename = f'data{FIR}.json'
    f = open(filename, 'r')
    dict = json.load(f)
    return dict

def import_json_avion(FIR, num_ligne):
    filename = f'avion{FIR}.json'
    f = open(filename, 'r')
    dicts = json.load(f)
    dict = dicts[num_ligne]
    return dict