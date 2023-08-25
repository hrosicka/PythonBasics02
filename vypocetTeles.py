from krychle import *
from koule import *

def main():

    while True:
        print("\nVýpočet povrchu a objemu krychle a koule")
        print("----------------------------------------")
        
        teleso = input("Zadej, které těleso chceš počítat: [krychle / koule]\n")
        teleso = teleso.lower()

        vlastnost = input("Zvolil jsi {}, chceš zjistit: [objem / povrch]\n".format(teleso))
        vlastnost = vlastnost.lower()

        if teleso == "krychle":
            rozmer = input("Zadej hranu krychle v centimetrech pro výpočet {}u\n".format(vlastnost))
        
        elif teleso == "koule":
            rozmer = input("Zadej poloměr koule v centimetrech pro výpočet {}u\n".format(vlastnost))

        else:
            break

        try:
            a = float(rozmer)
            if a < 0: 
                print("Vstup musí být kladné číslo, zkus to znovu!")
                continue
            break
        except ValueError:
            print("To není číslo! Zkus to znovu!")     


    
    if teleso == "krychle":
        mojeKrychle = Krychle(a)

        if vlastnost == "povrch":
            print(mojeKrychle.vypis()[0])
        
        elif vlastnost == "objem":
            print(mojeKrychle.vypis()[1])

        else:
            print("Špatné zadání!")


    elif teleso == "koule":
        mojeKoule = Koule(a)

        if vlastnost == "povrch":
            print(mojeKoule.vypis()[0])
        
        elif vlastnost == "objem":
            print(mojeKoule.vypis()[1])

        else:
            print("Špatné zadání!")

    else:
        print("Špatné zadání!")


if __name__ == "__main__":
    main()
