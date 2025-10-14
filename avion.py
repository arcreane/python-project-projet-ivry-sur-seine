import re

class avion:

    nb_avion = 0

    def __init__(self, callsign, phonetic, From, to, type, immat, turb, pax, final_level, sqwk, fuel, pos, heading, speed, vs, freq, conso, alt, route):
        self.callsign = callsign
        self.phonetic = phonetic
        self.From = From
        self.to = to
        self.type = type
        self.immat = immat
        self.turb = pax
        self.final_level = final_level
        self.sqwk = sqwk
        self.fuel = fuel
        self.pos = pos
        self.heading = heading
        self.speed = speed
        self.vs = vs
        self.freq = freq
        self.conso = conso
        self.alt = alt
        self.consigne = {'alt' : 0, 'heading' : None, 'speed' : None, 'vs' : None, 'freq' : 122.8}
        self.route = route
        avion.nb_avion += 1

    def horizontal(self):
        pass
    def vertical(self):
        pass
    def comm_tx(self):
        pass
    def comm_rx(self, receveid):
        if "climb" or "descend" in receveid:
            pass
        elif "turn left" or "turn right" in receveid:
            pass
        elif "accelerate" or "decelerate" in receveid:
            pass
        elif "increase" or "decrease" in receveid:
            pass
        elif "contact" in receveid:
            pass
    def exit(self):
        pass

    def __del__(self):
        avion.nb_avion -= 1



if __name__ == '__main__':
    Test = avion('Afr002 Heavy',
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
                 (5.0, 6.0),
                 000,
                 450,
                 0,
                 122.800,
                 7.5,
                 32000,
                 [(7.0,6.0), (10.0,6.0)])

