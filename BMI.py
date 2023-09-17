def indexBMI(hmotnost, vyska):
    """
    Výpočet Body Mass Indexu

    hmotnost - hmotnost v kg

    vyska - vyska postavy v metrech
    """
    
    if hmotnost > 0 and vyska > 0:
        bmi = hmotnost / pow(vyska,2)
        return bmi

    else:
        raise ValueError("Hmotnost musí být kladné číslo.")

def vypisHlasku(bmi):
    """
    Klasifikace tělesné hmotnosti

    bmi - body mass index
    """

    if bmi < 20:
        return "Podváha"
    
    elif bmi >= 20 and bmi < 25:
        return "Optimální váha"
    
    elif bmi >= 25 and bmi < 30:
        return "Nadváha"
    
    elif bmi >= 30 and bmi < 35:
        return "Obezita 1.stupeň"
    
    elif bmi >= 35 and bmi < 40:
        return "Obezita 2. stupeň"
    
    elif bmi >= 40:
        return "Morbidní obezita"
    
def main():

    bmi = round(indexBMI(52,1.57),2)
    print("BMI je", bmi)
    print(vypisHlasku(bmi))

if __name__ == "__main__":
    main()