import math

# třída koule
# počítá povrch, objem a vypisuje výsledek
# výsledek je vypsán v centimetrech, proto musí být vstup také v centimetrech
class Koule:
    
    # konstruktor - vytvoření koule
    def __init__(self, r):
        self.r = r

    # metoda pro výpočet povrchu koule
    def povrch(self):
        pov = 4 * math.pi * pow(self.r,2)
        return pov
    
    # metoda pro výpočet objemu koule
    def objem(self):
        obj = 4 * math.pi*pow(self.r, 3) / 3
        return obj

    # metoda pro vypsání povrchu a objemu koule - v centimetrech
    # vrací 2 řetězce - tuple formát
    def vypis(self):
        textPovrch = "Koule o poloměru {} cm má povrch {} cm2.".format(self.r, round(self.povrch(),3))
        textObjem = "Koule o poloměru {} cm má objem {} cm3.".format(self.r, round(self.objem(),3))
        return(textPovrch, textObjem)
