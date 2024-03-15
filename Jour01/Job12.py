a = int(input("Rentrez une première distance a : "))
b = int(input("Rentrez une première distance b : "))
c = int(input("Rentrez une première distance c : "))

if (a + b >= c) and (a + c >= b) and (b + c >= a):
    print("C'est un triangle c'est dejà pas mal")
    if a == b == c:
        print("C'est un triangle équilatéral")
    elif (a == b) or (a == c) or (b == c):
        if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            print("C'est un traingle isocèle rectangle")
        else:
            print("C'est un triangle isocèle")
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("C'est un triangle rectangle")
    else:
        print("C'est un triangle tout court")
else:
    print("Perdu ce n'est pas un triangle")