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

    def vertical(self):

    def comm_tx(self):

    def comm_rx(self, receveid):
        if "climb" or "descend" in receveid:

        elif "turn left" or "turn right" in receveid:

        elif "accelerate" or "decelerate" in receveid:

        elif "increase" or "decrease" in receveid:

        elif "contact" in receveid:

    def exit(self):


    def __str__(self):
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

