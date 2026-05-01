# numără vocalele
def numara_vocale (nume):
    vocale = "AEIOU"
    nr_vocale = 0
    for i in nume.upper():
        if i in vocale:
            nr_vocale += 1
    return nr_vocale

# verifică dacă un string conține numere
def contine_non_alpha(nume):
    return not nume.isalpha()

# introducere + validare nume
while True:
    nume_complet = input("Introduceţi numele şi prenumele utilizatorului: ").strip()
    nume_fragmentat = nume_complet.split(" ")
    if len(nume_fragmentat) >= 2:
        nume_incorect = None
        for nume in nume_fragmentat:
            if contine_non_alpha(nume):
                nume_incorect = nume

        if nume_incorect is not None:
            print(f"Componenta din nume {nume_incorect} conține cel puțin un caracter ce nu este litere")
            continue

        nume_incorect = None
        for nume in nume_fragmentat:
            if numara_vocale(nume) == 0:
                nume_incorect = nume

        if nume_incorect is not None:
            print(f"Componenta din nume {nume_incorect} nu conține vocale")
            continue

        break
    else:
        print("Numele nu a fost introdus corect. Asiguraţi-vă că introduceţi cel puţin două cuvinte.")

# introducere nr. de achiziții
while True:
    numar_achizitii = input("Introduceţi numărul de achiziţii din ultimul an: ").strip()
    if numar_achizitii.isnumeric() and int(numar_achizitii) > 0:
        numar_achizitii = int(numar_achizitii)
        break
    print("Introduceţi un număr pozitiv valid.")

# introducere sumă pt. fiecare achiziție
suma_totala = 0
achizitii_peste_10000 = 0

for i in range(1, numar_achizitii + 1):
    while True:
        suma = input(f"Introduceţi suma pentru achiziţia {i}: ").strip()
        suma = suma.replace(".", "")
        if suma.isnumeric():
            suma = float(suma)
            if suma > 0:
                suma_totala += suma
                if suma > 10000:
                    achizitii_peste_10000 += 1
                break
        print("Introduceţi o sumă pozitivă validă.")

# status utilizator
if suma_totala > 100000 and numar_achizitii > 10:
    statut = "VIP"
    reducere = 0.10
else:
    statut = "STANDARD"
    reducere = 0.05

# detalii utilizator
print(f"\nStimate {nume_complet}, aţi cheltuit în total {suma_totala:.2f} lei, "
      f"dintre care {achizitii_peste_10000} achiziţii au fost peste 10.000 de lei. "
      f"Utilizatorul {nume_complet} are statut de utilizator {statut}.")

# calculare reducere pt. o achiziție viitoare
while True:
    pret_articol = input("Introduceţi preţul articolului pe care doriţi să-l cumpăraţi: ").strip()
    if pret_articol.replace(".", "").replace(",", "").isnumeric():
        pret_articol = float(pret_articol.replace(",", "."))
        if pret_articol > 0:
            pret_cu_reducere = pret_articol * (1 - reducere)
            print(f"Preţul articolului cu reducere este: {pret_cu_reducere:.2f} lei.")
            break
    print("Introduceţi un preţ pozitiv valid.")
