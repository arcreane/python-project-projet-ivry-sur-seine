from math import sin, cos, radians, sqrt, acos, pi
from time import sleep

class Avion:

    nb_avion = 0

    def __init__(self, callsign, phonetic, from_, to, type_, immat, turb, pax, final_level, sqwk, fuel, pos, heading, speed, vs, conso, alt, ld_speed, aprt, random_nb):
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
        self.etat = {'can_land' : False, 'TCAS' : False}
        self.aprt_code = aprt
        self.random_nb = random_nb
        Avion.nb_avion += 1

    def horizontal_move(self):
        vx = (self.speed * sin(radians(self.heading)) / 3600) * 100
        vy = (self.speed * cos(radians(self.heading)) / 3600) * 100
        self.pos[0] += vx
        self.pos[1] -= vy

    def vertical_move(self):
        if self.consigne['alt'] is None:
            return

        # vitesse verticale en ft/s
        if self.consigne['vs'] is None:
            vs = 500 / 60
        else:
            vs = abs(self.consigne['vs']) / 60

        delta_alt = self.consigne['alt'] - self.alt

        if abs(delta_alt) <= vs:
            self.alt = self.consigne['alt']
        elif delta_alt > 0:
            self.alt += vs
        else:
            self.alt -= vs


    def heading_change(self):
        target = self.consigne['heading']

        # Normalisation : angle le plus court entre -180 et +180
        delta = (target - self.heading + 540) % 360 - 180

        angle_speed = 3  # taux de virage (° par cycle)

        if abs(delta) <= angle_speed:
            # On arrive pile au cap demandé
            self.heading = target % 360
        else:
            # Tourne à gauche ou à droite selon le plus court
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

    def exit_scope(self):
        if self.pos[0] <= 0 or self.pos[0] >= 1600:
            self.consigne['heading'] = (- self.heading) % 360  # rebond horizontal
        if self.pos[1] <= 0 or self.pos[1] >= 750:
            self.consigne['heading'] = (180 - self.heading) % 360  # rebond vertical

    def consigne_change(self, new):
        for k, v in new.items():
            if v is not None:
                self.consigne[k] = v

    def __del__(self):
        Avion.nb_avion -= 1


