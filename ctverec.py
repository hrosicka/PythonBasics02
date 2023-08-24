# třída čtverec
# počítá obvod, obsah a vypisuje výsledek
# výsledek je vypsán v centimetrech, proto musí být vstup také v centimetrech
class Ctverec:
    
    # konstruktor - vytvoření čtverce
    def __init__(self, a):
        self.a = a

    # metoda pro výpočet obvodu čtverce
    def obvod(self):
        obv = 4 * self.a
        return obv
    
    # metoda pro výpočet obsahu čtverce
    def obsah(self):
        obs = pow(self.a, 2)
        return obs

    # metoda pro vypsání obsahu a obvodu čtverce - v centimetrech
    # vrací 2 řetězce
    def vypis(self):
        textObvod = "Čtverec o straně {} cm má obvod {} cm.".format(self.a, self.obvod())
        textObsah = "Čtverec o straně {} cm má obsah {} cm2.".format(self.a, self.obsah())
        return(textObvod, textObsah)
