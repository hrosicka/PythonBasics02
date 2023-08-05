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
        textPovrch = "Krychle o straně {} cm má povrch {} cm2.".format(self.a, self.povrch())
        textObjem = "Krychle o straně {} cm má objem {} cm3.".format(self.a, self.objem())
        return(textPovrch, textObjem)
