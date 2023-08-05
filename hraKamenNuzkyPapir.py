# hra kámen nůžky papír - hráč proti počítači
# počítač náhodně vygeneruje čísla
from random import randrange

# funkce pro tah počítače, použije se random
def tahnulPocitac():
    # počítač náhodně vygeneruje čísla 0, 1 nebo 2, ze kterých se potom stanoví tah
    nahoda = randrange(0, 3)

    if nahoda == 0:
        tahPocitace = 'kámen'

    elif nahoda == 1:
        tahPocitace = 'nůžky'

    else:
        tahPocitace = 'papír'

    return tahPocitace
    
# funkce pro tah hráče
def tahnulHrac():

    # hráč musí zadat slovně svoji volbu
    tahHrace = input("Hraješ! Zadej buď kámen nůžky nebo papír: ")

    # pokud hráč zadá překlep, tak opakuje zadání dokud ho nezadá správně
    while ((tahHrace != 'kámen') and (tahHrace != 'nůžky') and (tahHrace != 'papír')):
        tahHrace = input("Zadal jsi to špatně! Zadej buď kámen nůžky nebo papír: ")

    return tahHrace


def main():

    print("\nHRA KÁMEN NŮŽKY PAPÍR")
    print("-------------------------------------------------------------------------")

    # hra se opakuje, dokud chce hráč hrát
    konec = False
    countHrac = 0
    countPocitac = 0

    

    while (konec != True):

        hralPocitac = tahnulPocitac()
        hralHrac = tahnulHrac()

        # vyhodnocení hry
        # tah hráče kámen
        if hralHrac == 'kámen' and hralPocitac == 'kámen':
            print("Remíza!!!")
        
        elif hralHrac == 'kámen' and hralPocitac == 'nůžky':
            countHrac = countHrac + 1
            print("Vyhrál jsi!!!")

        elif hralHrac == 'kámen' and hralPocitac == 'papír':
            countPocitac = countPocitac + 1
            print("Prohrál jsi!!!")

        # tah hráče nůžky
        elif hralHrac == 'nůžky' and hralPocitac == 'kámen':
            countPocitac = countPocitac + 1
            print("Prohrál jsi!!!")
        
        elif hralHrac == 'nůžky' and hralPocitac == 'nůžky':
            print("Remíza!!!")

        elif hralHrac == 'nůžky' and hralPocitac == 'papír':
            countHrac = countHrac + 1
            print("Vyhrál jsi!!!")

        # tah hráče papír
        elif hralHrac == 'papír' and hralPocitac == 'kámen':
            countHrac = countHrac + 1
            print("Vyhrál jsi!!!")
        
        elif hralHrac == 'papír' and hralPocitac == 'nůžky':
            countPocitac = countPocitac + 1
            print("Prohrál jsi!!!")

        elif hralHrac == 'papír' and hralPocitac == 'papír':
            print("Remíza!!!")
        

        print("\nAktuální skóre:")
        print("Počítač:", countPocitac)
        print("Ty:", countHrac)

        # dotaz na ukončení hry
        dotazNaKonec = input("\nChceš hrát dál? [ano/ne]")
        
        if dotazNaKonec == 'ano':
            konec = False
        
        else:
            konec = True

if __name__ == "__main__":
    main()
