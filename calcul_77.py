def determinare_statut(suma_totala, numar_achizitii):
    if suma_totala > 10000 and numar_achizitii > 5:
        return "PREMIUM"
    else:
        return "STANDARD"

# Cere numele clientului
while True:
    citire_nume = input("Introduceti numele si prenumele utilizatorului: ")
    if citire_nume.strip() != "":
        break
    else: 
        print("Eroare: Numele nu poate fi gol.")

# Cere numarul de achizitii
while True:
    try:
        numar_achizitii = int(input("Introduceti numarul de achizitii din ultimul an: "))
        if numar_achizitii > 0:
            break
        else:
            print("Eroare: Numarul de achizitii trebuie sa fie mai mare decat 0.")
    except ValueError:
        print("Eroare: Numarul de achizitii trebuie sa fie un numar intreg valid.")

# Initializeaza variabilele
suma_totala = 0
contor_achizitii_mari = 0

# Cere valorile pentru fiecare achizitie
for i in range(numar_achizitii):
    while True:
        try: 
            valoare_achizitie = float(input(f"Introduceti suma pentru achizitia {i+1}: "))
            suma_totala += valoare_achizitie
            if valoare_achizitie > 10000:
                contor_achizitii_mari += 1
            break
        except ValueError:
            print("Eroare: Valoarea achizitiei trebuie sa fie un numar valid.")

# Determina statutul
statut = determinare_statut(suma_totala, numar_achizitii)

# Afiseaza rezultatul conform hint-ului
nume_scurt = citire_nume.split()[0]
print(f"Stimate {nume_scurt}, ati cheltuit in total {suma_totala:,.1f}, dintre care {contor_achizitii_mari} achizitii au fost peste 10.000 de lei. Utilizatorul {citire_nume} are statut de utilizator {statut}.")

# Cere pretul articolului nou si aplica reducerea
while True:
    try:
        pret_articol = float(input(f"Stimate {nume_scurt}, introduceti pretul articolului pe care doriti sa-l cumparati: "))
        if statut == "PREMIUM":
            reducere = 0.10
        else:
            reducere = 0.05
        
        pret_cu_reducere = pret_articol * (1 - reducere)
        print(f"Pretul articolului cu reducere este: {pret_cu_reducere:.2f} lei.")
        break
    except ValueError:
        print("Eroare: Pretul trebuie sa fie un numar valid.")