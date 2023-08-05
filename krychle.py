class Krychle:
    
    def __init__(self, a):
        self.a = a

    def povrch(self):
        pov = 6 * pow(self.a,2)
        return pov
    
    def objem(self):
        obj = pow(self.a, 3)
        return obj

    def vypis(self):
        textPovrch = "Krychle o hraně {} cm má povrch {} cm2.".format(self.a, round(self.povrch(),3))
        textObjem = "Krychle o hraně {} cm má objem {} cm3.".format(self.a, round(self.objem(),3))
        return(textPovrch, textObjem)
