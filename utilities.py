from math import sqrt, atan2, degrees
import json

def distance_avion(plane_1, plane_2):
    delta_altitude = abs(plane_1.alt - plane_2.alt)
    distance = sqrt((plane_1.pos[0]-plane_2.pos[0])**2 + (plane_1.pos[1]-plane_2.pos[1])**2)
    return distance, delta_altitude


def import_json_data():
    filename = 'data.json'
    f = open(filename, 'r')
    list = json.load(f)
    dict = {}
    for dico in list:
        dict[dico['name']] = dico
    f.close()
    return dict

def import_json_avion(num_ligne):
    filename = 'avion.json'
    f = open(filename, 'r')
    dicts = json.load(f)
    dict = dicts[num_ligne]
    f.close()
    return dict

def json_data(FIR):
    filename = f'data{FIR}.json'
    f = open(filename, 'r')
    f2 = open('data.json', 'w')
    dict = json.load(f)
    json.dump(dict, f2)
    f.close()
    f2.close()


def json_avion(FIR):
    filename = f'avion{FIR}.json'
    f = open(filename, 'r')
    f2 = open('avion.json', 'w')
    dict = json.load(f)
    json.dump(dict, f2)
    f.close()
    f2.close()

