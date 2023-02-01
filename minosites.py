def beker():
    muzeum = input("Múzeum neve: ")
    latogato = input("Látogató neve: ")
    ertekeles = int(input("Értékelés (1-20): "))


    print("\nI/A: ")
    print(f"\tMúzeum neve: {muzeum}")
    print(f"\tLátogató neve: {latogato}")
    print(f"\tÉrtékelés (1-20): {ertekeles}")

    print("I/B: ")
    if ertekeles <= 0:
        print("\tAz értékelés nem lehet negatív vagy 0!\n")
    elif ertekeles > 20:
        print("\t20 pont feletti értékelés nem elfogadható!\n")
    else:
        print("\tKöszönjük az értékelést!\n")


