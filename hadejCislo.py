def nactiCislo():
    """
    Načte hádané číslo
    """
    while True:
        number = input("Hádej celé číslo: ")
        try:
            a = int(number)
            return a
        except ValueError:
            print("To není celé číslo! Zkus to znovu!")
       
def vypisVysledek(hadaneCislo, tipnuteCislo):
    """
    Vypíše výsledek hádání
    
    hadaneCislo - číslo, které uživatel hádá

    tipnuté číslo - číslo, které si uživatel tipnul
    """
    if hadaneCislo == tipnuteCislo:
        print("COOL!!! Uhodl jsi správně číslo {}".format(hadaneCislo))
    else:
        rozdíl = abs(hadaneCislo - tipnuteCislo)
        print("Smůla. Jsi takto daleko: {0}, hádané číslo je {1}".format(rozdíl, hadaneCislo))

def main():

    cislo = -537
    tip = nactiCislo()
    vypisVysledek(cislo, tip)

if __name__ == "__main__":
    main()