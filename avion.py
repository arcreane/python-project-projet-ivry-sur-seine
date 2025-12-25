from math import sin, cos, radians, sqrt
from utilities import import_json_data

class Avion:

    nb_avion = 0

    def __init__(self, callsign, phonetic, from_, to, type_, immat, turb, pax, final_level, sqwk, fuel, pos, heading, speed, vs, conso, alt, ld_speed, aprt, random_nb, max):
        self.callsign = callsign
        self.phonetic = phonetic
        self.from_ = from_
        self.to = to
        self.type_ = type_
        self.immat = immat
        self.turb = turb
        self.pax = pax
        self.final_level = final_level
        self.sqwk = sqwk
        self.fuel = fuel
        self.pos = pos
        self.heading = heading % 360
        self.speed = speed
        self.vs = vs
        self.conso = conso
        self.alt = alt
        self.landing_speed = ld_speed
        self.consigne = {'alt' : alt, 'heading' : heading % 360, 'speed' : speed, 'vs' : vs, 'landing' : False}
        self.etat = {'can_land' : False, 'TCAS' : False, 'land ?' : False}
        self.aprt_code = aprt
        self.random_nb = random_nb
        self.emergency = 'Normal'
        self.max = max
        Avion.nb_avion += 1

    def horizontal_move(self):
        vx = (self.speed * sin(radians(self.heading)) / 3600) * 75
        vy = (self.speed * cos(radians(self.heading)) / 3600) * 75
        self.pos[0] += vx
        self.pos[1] -= vy
        self.fuel -= self.conso / 3600

    def vertical_move(self):
        alt = self.alt
        if self.consigne['alt'] is not None:
                self.vs = self.consigne['vs']
        if self.vs is None or self.vs == 0:
            vs = 1500 / 60
        else:
            vs = self.vs / 60
        delta_alt = self.alt - self.consigne['alt']
        if delta_alt < 0:
            if abs(delta_alt) > abs(vs):
                alt += round(abs(vs))
            else:
                alt = round(self.consigne['alt'])
        if delta_alt > 0:
            if abs(delta_alt) > abs(vs):
                alt -= round(abs(vs))
            else:
                alt = round(self.consigne['alt'])
        self.alt = round(alt)



    def heading_change(self):
        target = self.consigne['heading']
        delta = (target - self.heading + 540) % 360 - 180

        angle_speed = 3

        if abs(delta) <= angle_speed:
            self.heading = target % 360
        else:
            self.heading = (self.heading + angle_speed * (1 if delta > 0 else -1)) % 360


    def speed_change(self):
        if self.alt <= 10000 and (self.consigne['speed'] is None or self.consigne['speed'] > 250):
            self.consigne['speed'] = 250
        if self.consigne['speed'] is not None:
            delta_speed = self.speed - self.consigne['speed']
            if delta_speed < 0:
                if delta_speed < 5:
                    self.speed += 5
                else:
                    self.speed = self.consigne['speed']
            elif delta_speed > 0:
                if delta_speed > 5:
                    self.speed -= 5
                else:
                    self.speed = self.consigne['speed']


    def vs_change(self):
        if self.consigne['vs'] is not None:
            delta_vs = self.vs - self.consigne['vs']
            if delta_vs < 0:
                if delta_vs < -150:
                    self.vs += 150
                else:
                    self.vs = self.consigne['vs']
            elif delta_vs > 0:
                if delta_vs > -150:
                    self.vs -= 150
                else:
                    self.vs = self.consigne['vs']

    def distance_airport(self):
        airport_infos = self.to
        distance = sqrt((self.pos[0] - airport_infos[0]) ** 2 + (self.pos[1] - airport_infos[1]) ** 2)
        if distance < 80:
            self.etat['can_land'] = True
        else:
            self.etat['can_land'] = False
        return distance

    def exit_scope(self):
        pts = import_json_data()
        max_x = max(pts['ALPHA']['pos_x'], pts['BRAVO']['pos_x'], pts['CHARLIE']['pos_x'], pts['DELTA']['pos_x'], pts['ECHO']['pos_x'], pts['FOXTROT']['pos_x']) + 5
        min_x = min(pts['ALPHA']['pos_x'], pts['BRAVO']['pos_x'], pts['CHARLIE']['pos_x'], pts['DELTA']['pos_x'], pts['ECHO']['pos_x'], pts['FOXTROT']['pos_x']) - 5
        max_y = max(pts['ALPHA']['pos_y'], pts['BRAVO']['pos_y'], pts['CHARLIE']['pos_y'], pts['DELTA']['pos_y'], pts['ECHO']['pos_y'], pts['FOXTROT']['pos_y']) + 5
        min_y = min(pts['ALPHA']['pos_y'], pts['BRAVO']['pos_y'], pts['CHARLIE']['pos_y'], pts['DELTA']['pos_y'], pts['ECHO']['pos_y'], pts['FOXTROT']['pos_y']) - 5
        if self.pos[0] <= min_x or self.pos[0] >= max_x:
            self.heading = (- self.heading) % 360  # rebond horizontal
            self.consigne['heading'] = self.heading
        if self.pos[1] <= min_y or self.pos[1] >= max_y:
            self.heading = (180 - self.heading) % 360  # rebond vertical
            self.consigne['heading'] = self.heading


    def consigne_change(self, new):
        for k, v in new.items():
            if v is not None:
                self.consigne[k] = v

    def __del__(self):
        Avion.nb_avion -= 1