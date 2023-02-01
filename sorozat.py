import random
vel_lista = []

#A. Írasson ki a konzolra csillag jellel (*) elválasztva 15 számból álló véletlen számsorozatot
# [-90,500] zárt intervallumon a mintának megfelelően.
def kiir():
    i= 0
    szoveg = ""
    while i < 15:
        vel = int(random.random() *  591) - 90
        vel_lista.append(vel)
        if i == 14:
            szoveg += str(vel)
        else:
            szoveg += str(vel) + "*"
        i += 1

    print("II/A, B, C: ")
    print(f"\t {szoveg}")



def oszthatoak_szama(vel_lista):
    i = 0
    oszthato_db = 0
    while i < len(vel_lista):
        if vel_lista[i] % 10 == 0:
            oszthato_db += 1
        i += 1
    return oszthato_db

def konzolra_ir():
    print("II/D, E: ")
    print(f"\tTízzel osztható számok száma: {oszthatoak_szama(vel_lista)}")

def fajl_ir():
    fajlom = open("kimutatas.txt", "w", encoding="utf-8")
    fajlom.write(f"kimutatas.txt tartalma:\nII/F:\n \tTízzel osztható számok száma: {oszthatoak_szama(vel_lista)}.")
    fajlom.close()
    print(" ")








