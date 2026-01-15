import os
import glob

# otsib failid kasutaja antud laiendi järgi
def leia_projektifailid():
    fail = input("sisesta faililaiendi ilma punktita: ")
    failid = glob.glob(f'*.{fail}')
    print(f"leitud failid: {failid}")
    return f".{fail} failid: {failid}"

# analüüsib faili sisu ja otsib kindlat sõna
def analuusi_faili_sisu():
    while True:
        failitee = input("sisesta faili tee: ")
        if not os.path.isfile(failitee):
            print("faili ei leitud, proovi uuesti.")
        else:
            fail = open(failitee, 'r', encoding='utf-8')
            sisu = fail.read()
            sõna = input("sisesta sõna, mida otsida: ")
            sõna_count = sisu.lower().count(sõna.lower())
            length = len(sisu)
            fail.close()

            print(f"sisu: {sisu}")
            print(f"sõna '{sõna}' esinemiste arv: {sõna_count}")
            print(f"faili pikkus: {length} tähemärki")
            break

    return f"{sõna_count}\nfaili pikkus: {length}\nsisu failist:\n{sisu}\n"

# loob, kustutab või otsib kataloogi
def loo_raporti_kataloog():
    while True:
        failitee = input("sisesta raporti kataloogi tee: ")
        ask = input("kas soovid lisada või kustutada või otsida kataloogi? (l/k/o): ").lower()

        if ask == 'l':
            if not os.path.isdir(failitee):
                os.mkdir(failitee)
                return f"kataloog {failitee} on loodud"
            else:
                print("kataloog on juba olemas.")
                break

        elif ask == 'k':
            if not os.path.isdir(failitee):
                print("kataloogi ei leitud.")
            else:
                ask2 = input("kas soovid kindlasti kustutada? (jah/ei): ").lower()
                if ask2 == 'jah':
                    os.rmdir(failitee)
                    return f"kataloog {failitee} on kustutatud"
                else:
                    print("kustutamine katkestatud.")
                    break

        elif ask == 'o':
            if os.path.isdir(failitee):
                print(f"kataloog {failitee} on leitud.")
                return f"{failitee} on leitud"
            else:
                print("kataloogi ei leitud.")
                break

# otsib failid algustähe järgi
def leia_failid_algustahega():
    while True:
        algustaht = input("sisesta algustäht: ")
        if not algustaht.isalpha() or len(algustaht) != 1:
            print("palun sisesta üks täht.")
        else:
            break

    failid = glob.glob(f'{algustaht}*')
    print(f"leitud failid: {failid}")
    return f"algustähega {algustaht} failid:\n{failid}\nkokku: {len(failid)}"

# loob, kustutab või otsib faili
def loo_raporti_Faiili():
    while True:
        failitee = input("sisesta raporti faili tee: ")
        ask = input("kas soovid lisada(l), kustutada(k) või otsida(o) faili? (l/k/o): ").lower()

        if ask == 'l':
            if not os.path.isfile(failitee):
                open(failitee, 'w', encoding='utf-8').close()
                return f"fail {failitee} on loodud"
            else:
                print("fail on juba olemas.")
                break

        elif ask == 'k':
            if not os.path.isfile(failitee):
                print("faili ei leitud.")
            else:
                ask2 = input("kas soovid kindlasti kustutada? (jah/ei): ").lower()
                if ask2 == 'jah':
                    os.unlink(failitee)
                    return f"fail {failitee} on kustutatud"
                else:
                    print("kustutamine katkestatud.")
                    break

        elif ask == 'o':
            for juur, kaustad, failid in os.walk('.'):
                if failitee in failid:
                    tee = os.path.abspath(os.path.join(juur, failitee))
                    print(f"faili asukoht: {tee}")
                    return f"{tee} on leitud"

            print("faili ei leitud.")
            break
