
print("JEDNODUCHÁ KALKULAČKA")
print("---------------------")
prvniCislo = float(input("Zadejte první číslo: "))
druheCislo = float(input("Zadejte druhé číslo: "))

soucet = prvniCislo + druheCislo
rozdil = prvniCislo - druheCislo
soucin = prvniCislo * druheCislo


print('Součet:\t\t\t%.3f + %.3f = %.3f' % (prvniCislo, druheCislo, soucet))
print('Rozdíl:\t\t\t%.3f - %.3f = %.3f' % (prvniCislo, druheCislo, rozdil))
print('Součin:\t\t\t%.3f * %.3f = %.3f' % (prvniCislo, druheCislo, soucin))


if (druheCislo != 0):
    podil = prvniCislo / druheCislo
    print('Podíl:\t\t\t%.3f / %.3f = %.3f' % (prvniCislo, druheCislo, podil))
    celociselneDeleni = prvniCislo // druheCislo
    print('Celočíselné dělení:\t%.3f // %.3f = %.3f' % (prvniCislo, druheCislo, celociselneDeleni))
    zbytek = prvniCislo % druheCislo
    print('Zbytek po dělení:\t%.3f // %.3f = %.3f' % (prvniCislo, druheCislo, zbytek))

    
else:
    print('Podíl:\t\t\t%.3f / %.3f = ???' % (prvniCislo, druheCislo))
    print("Nulou nelze dělit!!!")

umocneni = prvniCislo ** druheCislo
print('Umocnění:\t\t%.3f ** %.3f = %.3f' % (prvniCislo, druheCislo, umocneni))