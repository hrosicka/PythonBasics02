from ctverec import *
from kruh import *
from krychle import *

def main():

    while True:
        print("\nVýpočet obsahu a obvodu čtverce a kruhu a také povrchu a objemu krychle")
        print("-------------------------------------------------------------------------")
        number = input("Zadej stranu čtverce (poloměr kruhu, stranu krychle) v cm: ")
        try:
            a = float(number)
            if a < 0: 
                print("Vstup musí být kladné číslo, zkus to znovu!")
                continue
            break
        except ValueError:
            print("To není číslo! Zkus to znovu!")     
            
    mujCtverec = Ctverec(a)
    mujKruh = Kruh(a)
    mojeKrychle = Krychle(a)
    print(mujCtverec.vypis()[0])
    print(mujCtverec.vypis()[1])
    print(mujKruh.vypis()[0])
    print(mujKruh.vypis()[1])
    print(mojeKrychle.vypis()[0])
    print(mojeKrychle.vypis()[1])


if __name__ == "__main__":
    main()
