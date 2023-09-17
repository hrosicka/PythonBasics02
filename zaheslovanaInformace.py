def main():

    heslo = "333StribrnychStrikacek"
    
    while True:
        uzivatel = input("Zadej tajné heslo: ")
        if heslo == uzivatel:
            print("V pátek jsme byli na koupališti a viděli velkou sovu.")
            break
        else:
            print("Chybné heslo")

if __name__ == "__main__":
    main()
