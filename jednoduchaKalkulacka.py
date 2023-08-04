
print("JEDNODUCHÁ KALKULAČKA")
print("---------------------")
prvniCislo = float(input("Zadejte první číslo: "))
druheCislo = float(input("Zadejte druhé číslo: "))

soucet = prvniCislo - druheCislo
rozdil = prvniCislo - druheCislo
soucin = prvniCislo * druheCislo


print('%.3f + %.3f = %.3f' % (prvniCislo, druheCislo, soucet))
print('%.3f - %.3f = %.3f' % (prvniCislo, druheCislo, rozdil))
print('%.3f * %.3f = %.3f' % (prvniCislo, druheCislo, soucin))


if (druheCislo != 0):
    podil = prvniCislo / druheCislo
    print('%.3f / %.3f = %.3f' % (prvniCislo, druheCislo, podil))
    
else:
    print('%.3f / %.3f = ???' % (prvniCislo, druheCislo))
    print("Nulou nelze dělit!!!")
