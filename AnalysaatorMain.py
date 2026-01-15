# peaprogramm failide ja kataloogide analüüsimiseks
import AnalysaatorModule
import os

print(os.getcwd())

failid = os.listdir()
laiendid = set()
for f in failid:
    if '.' in f:
        laiendid.add(f.split('.')[-1])

# siia kogutakse kasutaja valikute tulemused
stat = []

# menüüga põhitsükkel
while True:
    valik = input(
        "vali tegevus:\n"
        "1. otsi projektifaile\n"
        "2. analüüsi faili sisu\n"
        "3. loo kataloogi raport\n"
        "4. otsi faile algustähega\n"
        "5. faili haldus\n"
        "6. salvesta ja välju\n"
        "sisesta valik (1-6): "
    )

    if valik not in ['1', '2', '3', '4', '5', '6']:
        print("vigane valik, proovi uuesti.")
        continue

    try:
        if valik == '1':
            stat.append(AnalysaatorModule.leia_projektifailid())
        elif valik == '2':
            stat.append(AnalysaatorModule.analuusi_faili_sisu())
        elif valik == '3':
            stat.append(AnalysaatorModule.loo_raporti_kataloog())
        elif valik == '4':
            stat.append(AnalysaatorModule.leia_failid_algustahega())
        elif valik == '5':
            stat.append(AnalysaatorModule.loo_raporti_Faiili())
        elif valik == '6':
            print("väljun...")
            break

    except Exception as e:
        print("ilmnes viga, proovi uuesti. viga:", e)

# statistika salvestamine faili
if os.path.isfile('statistika.txt'):
    os.unlink("statistika.txt")

with open("statistika.txt", 'w', encoding='utf-8') as f:
    for rida in stat:
        f.write(str(rida) + "\n")

print("statistika on salvestatud faili 'statistika.txt'.")
