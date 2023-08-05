import math

class Koule:
    
    def __init__(self, r):
        self.r = r

    def povrch(self):
        pov = 4 * math.pi * pow(self.r,2)
        return pov
    
    def objem(self):
        obj = 4 * math.pi*pow(self.r, 3) / 3
        return obj

    def vypis(self):
        textPovrch = "Koule o poloměru {} cm má povrch {} cm2.".format(self.r, round(self.povrch(),3))
        textObjem = "Koule o poloměru {} cm má objem {} cm3.".format(self.r, round(self.objem(),3))
        return(textPovrch, textObjem)
