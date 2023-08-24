# třída krychle
# počítá povrch, objem a vypisuje výsledek
# výsledek je vypsán v centimetrech, proto musí být vstup také v centimetrech
class Krychle:
    
    # konstruktor - vytvoření krychle
    def __init__(self, a):
        self.a = a

    # metoda pro výpočet povrchu krychle
    def povrch(self):
        pov = 6 * pow(self.a,2)
        return pov
    
    # metoda pro výpočet objemu krychle
    def objem(self):
        obj = pow(self.a, 3)
        return obj

    # metoda pro vypsání povrchu a objemu krychle - v centimetrech
    # vrací 2 řetězce - tuple formát
    def vypis(self):
        textPovrch = "Krychle o hraně {} cm má povrch {} cm2.".format(self.a, round(self.povrch(),3))
        textObjem = "Krychle o hraně {} cm má objem {} cm3.".format(self.a, round(self.objem(),3))
        return(textPovrch, textObjem)
