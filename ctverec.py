class Ctverec:
    
    def __init__(self, a):
        self.a = a

    def obvod(self):
        obv = 4 * self.a
        return obv
    
    def obsah(self):
        obs = pow(self.a, 2)
        return obs

    def vypis(self):
        textObvod = "Čtverec o straně {} cm má obvod {} cm.".format(self.a, self.obvod())
        textObsah = "Čtverec o straně {} cm má obsah {} cm2.".format(self.a, self.obsah())
        return(textObvod, textObsah)
