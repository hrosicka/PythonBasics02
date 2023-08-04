import math
class Kruh:
    
    def __init__(self, r):
        self.r = r

    def obvod(self):
        obv = 2 * math.pi * self.r
        return obv
    
    def obsah(self):
        obs = math.pi * pow(self.r, 2)
        return obs

    def vypis(self):
        textObvod = "Kruh o poloměru {} cm má obvod {} cm.".format(self.r, round(self.obvod(), 3))
        textObsah = "Kruh o poloměru {} cm má obsah {} cm2.".format(self.r, round(self.obsah(), 3))
        return(textObvod, textObsah)
