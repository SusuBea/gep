from Gep import Gep
gep_lista = []

def beolvasas():
    fajlom = open("gep.txt", "r", encoding="utf-8")
    fejlec = fajlom.readline()
    sorok = fajlom.readlines()
    fajlom.close()
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("!")
        gep_lista.append(Gep(sor))
        i += 1

def gepek_szama():
    print("III/A, B: ")
    print(f"\tA gépek száma: {len(gep_lista)}.")

def atlag():
    i = 0
    db = 0
    sum = 0
    while i < len(gep_lista):
        if gep_lista[i].id % 2 == 0:
            db += 1
            sum += gep_lista[i].id
        i += 1
    atlag = sum / db
    print("III/C: ")
    print(f"\t A páros teremszámú termek azonosító átlaga: {int(atlag)}.")

def legkisebb():
    i = 0
    legkisebb = 0
    while i < len(gep_lista):
        if gep_lista[legkisebb].id > gep_lista[i].id:
            legkisebb = i
        i += 1
    print("III/D: ")
    print(f"\tA legkisebb asztali gép azonosítója: {gep_lista[legkisebb].id}, helye: {gep_lista[legkisebb].hely}.")





