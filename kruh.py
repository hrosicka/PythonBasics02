import math

# třída kruh
# počítá obvod, obsah a vypisuje výsledek
# výsledek je vypsán v centimetrech, proto musí být vstup také v centimetrech
class Kruh:
    
    # konstruktor - vytvoření kruhu
    def __init__(self, r):
        self.r = r

    # metoda pro výpočet obvodu kruhu
    def obvod(self):
        obv = 2 * math.pi * self.r
        return obv
    
    # metoda pro výpočet obsahu kruhu
    def obsah(self):
        obs = math.pi * pow(self.r, 2)
        return obs

    # metoda pro vypsání obsahu a obvodu kruhu - v centimetrech
    # vrací 2 řetězce
    def vypis(self):
        textObvod = "Kruh o poloměru {} cm má obvod {} cm.".format(self.r, round(self.obvod(), 3))
        textObsah = "Kruh o poloměru {} cm má obsah {} cm2.".format(self.r, round(self.obsah(), 3))
        return(textObvod, textObsah)
