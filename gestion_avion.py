from avion import Avion
from fonction_json import import_json
from random import randint
from time import sleep

FIR = "reims"
L = []
dict_avion = {}
ALPHA = [0, 0]
BRAVO = [0, 0]
CHARLIE = [0, 0]
DELTA = [0, 0]
ECHO = [0, 0]
FOXTROT = [0, 0]
GOLF = [0, 0]

count = 0

while count != 2:
    while len(dict_avion.keys()) <= 4:
        for i in range(5 + 1):
            if i not in dict_avion.keys():
                n = randint(0, 6)
                while n in L:
                    n = randint(0, 6)
                L.append(n)
                dict_cara = import_json(FIR, n)
                match dict_cara['pos']:
                    case 'ALPHA':
                        position = ALPHA
                    case 'BRAVO':
                        position = BRAVO
                    case 'CHARLIE':
                        position = CHARLIE
                    case 'DELTA':
                        position = DELTA
                    case 'ECHO':
                        position = ECHO
                    case 'FOXTROT':
                        position = FOXTROT
                    case 'GOLF':
                        position = GOLF
                    case _ :
                        position = ALPHA
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
                                                position,
                                                int(dict_cara['heading']),
                                                int(dict_cara['speed']),
                                                int(dict_cara['vs']),
                                                float(dict_cara['conso']),
                                                int(dict_cara['alt']))


    for key in dict_avion.keys():
        dict_avion[key].heading_change()
        dict_avion[key].speed_change()
        dict_avion[key].vs_change()
        dict_avion[key].horizontal_move()
        dict_avion[key].vertical_move()

        print(dict_avion[key].callsign)
        print(dict_avion[key].heading)
        print(dict_avion[key].speed)
        print(dict_avion[key].vs)
        print(dict_avion[key].pos)
        print(dict_avion[key].alt, '\n')

    sleep(1)
    count += 1