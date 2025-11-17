from math import sin, cos, radians

class Avion:

    nb_avion = 0

    def __init__(self, callsign, phonetic, from_, to, type_, immat, turb, pax, final_level, sqwk, fuel, pos, heading, speed, vs, conso, alt):
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
        self.consigne = {'alt' : None, 'heading' : None, 'speed' : None, 'vs' : None}
        Avion.nb_avion += 1

    def horizontal_move(self):
        vx = round((self.speed * sin(radians(self.heading)) / 3600) * 100)
        vy = round((self.speed * cos(radians(self.heading)) / 3600) * 100)
        self.pos[0] += vx
        self.pos[1] += vy


    def vertical_move(self):
        if self.consigne['alt'] is not None:
            vs = self.vs / 60
            delta_alt = self.alt - self.consigne['alt']
            if  delta_alt < 0:
                if delta_alt < vs :
                    self.alt += vs
                else:
                    self.alt = self.consigne['alt']
            if delta_alt > 0:
                if delta_alt > vs:
                    self.alt -= vs
                else:
                    self.alt = self.consigne['alt']

    def heading_change(self):
        if self.consigne['heading'] is not None:
            delta_angle = self.consigne['heading'] - self.heading
            angle_speed = 3
            if 0 < delta_angle <= 180:
                if abs(delta_angle) > 3:
                    self.heading += angle_speed
                    self.heading %= 360
                else:
                    self.heading = self.consigne['heading']
            elif 360 > delta_angle > 180:
                if abs(delta_angle) > 3:
                    self.heading -= angle_speed
                    self.heading %= 360
                else:
                    self.heading = self.consigne['heading']
            elif delta_angle < 0:
                if abs(delta_angle) > 3:
                    self.heading += angle_speed
                    self.heading %= 360
                else:
                    self.heading = self.consigne['heading']

    def speed_change(self):
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



    def __del__(self):
        Avion.nb_avion -= 1



if __name__ == '__main__':
    Test = Avion('Afr002 Heavy',
                 'air frans',
                 'LFPG',
                 'KJFK',
                 'B777',
                 'F-GSPZ',
                 'Heavy',
                 312,
                 360,
                 1000,
                 53.2,
                 [0.0, 0.0],
                 000,
                 450,
                 0,
                 7.5,
                 32000,
                 )

    def test():
        Test.consigne = {'alt' : 31850, 'heading' : 3, 'speed' : 455, 'vs' : 150}
        Test.heading_change()
        Test.speed_change()
        Test.vs_change()
        Test.horizontal_move()
        Test.vertical_move()
        print(f'Heading: {Test.heading}\n')
        print(f'Speed: {Test.speed}\n')
        print(f'VS: {Test.vs}\n')
        print(f'Pos: {Test.pos}\n')
        print(f'Alt: {Test.alt}')

    test()