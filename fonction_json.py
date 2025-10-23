import json

def import_json(FIR, num_ligne):
    filename = f'data{FIR}.json'
    f = open(filename, 'r')
    dicts = json.load(f)
    dict = dicts[num_ligne]
    return dict