from ctverec import *
from kruh import *

def main():

    while True:
        print("\nVýpočet obsahu a obvodu čtverce a kruhu")
        print("-------------------------------")
        number = input("Zadej stranu čtverce (poloměr kruhu) v cm: ")
        try:
            a = float(number)
            if a < 0: 
                print("Vstup musí být kladné číslo, zkus to znovu!")
                continue
            break
        except ValueError:
            print("To není číslo! Zkus to znovu!")     
    # else all is good, val is >=  0 and an integer
    mujCtverec = Ctverec(a)
    mujKruh = Kruh(a)
    print(mujCtverec.vypis()[0])
    print(mujCtverec.vypis()[1])
    print(mujKruh.vypis()[0])
    print(mujKruh.vypis()[1])


if __name__ == "__main__":
    main()
