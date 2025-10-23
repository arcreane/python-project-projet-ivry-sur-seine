import avion

dict_avion = {
"avion0" : avion.Avion(),
"avion1" : avion.Avion(),
"avion2" : avion.Avion(),
"avion3" : avion.Avion(),
"avion4" : avion.Avion(),
}

while True:
    while len(dict_avion.keys()) <= 4:
        for i in range(5 + 1):
            if f'avion{i}' not in dict_avion.keys():
                dict_avion[f'avion{i}'] = avion.Avion()

    for key in dict_avion.keys():
        dict_avion[key] .heading_change()
        dict_avion[key] .speed_change()
        dict_avion[key] .vs_change()
        dict_avion[key] .horizontal_move()
        dict_avion[key] .vertical_move()