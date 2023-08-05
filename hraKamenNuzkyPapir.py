# hra kámen nůžky papír - hráč proti počítači
# počítač náhodně vygeneruje čísla
from random import randrange

def main():

    print("\nHRA KÁMEN NŮŽKY PAPÍR")
    print("-------------------------------------------------------------------------")

    # hra se opakuje, dokud chce hráč hrát
    konec = False
    countHrac = 0
    countPocitac = 0

    while (konec != True):

        # počítač náhodně vygeneruje čísla 0, 1 nebo 2, ze kterých se potom stanoví tah
        nahoda = randrange(0, 3)

        if nahoda == 0:
            tahPocitace = 'kámen'

        elif nahoda == 1:
            tahPocitace = 'nůžky'

        else:
            tahPocitace = 'papír'
        
        # hráč musí zadat slovně svoji volbu
        tahHrace = input("Hraješ! Zadej buď kámen nůžky nebo papír: ")

        # pokud hráč zadá překlep, tak opakuje zadání dokud ho nezadá správně
        while ((tahHrace != 'kámen') and (tahHrace != 'nůžky') and (tahHrace != 'papír')):
            tahHrace = input("Zadal jsi to špatně! Zadej buď kámen nůžky nebo papír: ")

        # vyhodnocení hry
        # tah hráče kámen
        if tahHrace == 'kámen' and tahPocitace == 'kámen':
            print("Remíza!!!")
        
        elif tahHrace == 'kámen' and tahPocitace == 'nůžky':
            countHrac = countHrac + 1
            print("Vyhrál jsi!!!")

        elif tahHrace == 'kámen' and tahPocitace == 'papír':
            countPocitac = countPocitac + 1
            print("Prohrál jsi!!!")

        # tah hráče nůžky
        elif tahHrace == 'nůžky' and tahPocitace == 'kámen':
            countPocitac = countPocitac + 1
            print("Prohrál jsi!!!")
        
        elif tahHrace == 'nůžky' and tahPocitace == 'nůžky':
            print("Remíza!!!")

        elif tahHrace == 'nůžky' and tahPocitace == 'papír':
            countHrac = countHrac + 1
            print("Vyhrál jsi!!!")

        # tah hráče papír
        elif tahHrace == 'papír' and tahPocitace == 'kámen':
            countHrac = countHrac + 1
            print("Vyhrál jsi!!!")
        
        elif tahHrace == 'papír' and tahPocitace == 'nůžky':
            countPocitac = countPocitac + 1
            print("Prohrál jsi!!!")

        elif tahHrace == 'papír' and tahPocitace == 'papír':
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
