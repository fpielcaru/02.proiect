from eveniment import Eveniment
import os 

def incarca_evenimente(evenimente, filename):
    """Încarcă evenimentele din fișier la pornire"""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    # Atenție: fără spațiu după virgulă
                    nume, data, locatie, nr_bilete, pret_bilet = line.split(",")
                    eveniment = Eveniment(nume.strip(), data.strip(), locatie.strip(), 
                                          int(nr_bilete.strip()), float(pret_bilet.strip()))
                    evenimente.append(eveniment)

def salveaza_evenimente(evenimente, filename):
    """Salvează toate evenimentele în fișier"""
    with open(filename, "w") as f:
        for eveniment in evenimente:
            # Fără spațiu după virgulă ca să se potrivească cu split-ul de la citire
            f.write(f"{eveniment.nume},{eveniment.data},{eveniment.locatie},{eveniment.nr_bilete},{eveniment.pret_bilet}\n")

def adauga_eveniment(evenimente, filename):
    """Adaugă eveniment nou și salvează automat"""
    try:
        nume = input("Numele evenimentului: ")
        data = input("Data evenimentului (ZZ/LL/AAAA): ")
        locatie = input("Locatia evenimentului: ")
        nr_bilete = int(input("Numarul de bilete vandute: "))
        pret_bilet = float(input("Pretul biletului: "))
        
        eveniment = Eveniment(nume, data, locatie, nr_bilete, pret_bilet)
        evenimente.append(eveniment)
        salveaza_evenimente(evenimente, filename)  # Salvează automat
        print("Eveniment adăugat cu succes!\n")
        
    except ValueError as e:
        print(f"Eroare: {e}\n")

def afiseaza_evenimente(evenimente):
    """Afișează toate evenimentele cu numere de ordine"""
    if not evenimente:
        print("Nu există evenimente.\n")
        return
    
    for i, eveniment in enumerate(evenimente):
        print(f"{i+1}. {eveniment}")
    print()

def cauta_eveniment(evenimente):
    """Caută eveniment după nume (căutare parțială)"""
    cautat = input("Introdu numele evenimentului căutat: ").lower()
    gasite = []
    
    for eveniment in evenimente:
        if cautat in eveniment.nume.lower():
            gasite.append(eveniment)
    
    if gasite:
        print(f"Am găsit {len(gasite)} eveniment(e):")
        for e in gasite:
            print(f"  - {e}")
        print()
    else:
        print("Nu s-a găsit niciun eveniment.\n")

def evenimente_viitoare(evenimente):
    """Afișează evenimentele cu data mai mare decât data curentă"""
    data_curenta = input("Data curenta (ZZ/LL/AAAA): ")
    viitoare = []
    
    for eveniment in evenimente:
        if eveniment.data > data_curenta:
            viitoare.append(eveniment)
    
    if viitoare:
        print(f"Evenimente viitoare ({len(viitoare)}):")
        for e in viitoare:
            print(f"  - {e}")
        print()
    else:
        print("Nu există evenimente viitoare.\n")

def total_incasari(evenimente):
    """Afișează totalul încasărilor din toate evenimentele"""
    if not evenimente:
        print("Nu există evenimente.\n")
        return
    
    total = 0
    for eveniment in evenimente:
        total += eveniment.calculeaza_incasari()
    
    print(f"Total încasări: {total} lei\n")

def main():
    evenimente = []
    filename = "evenimente.txt"
    
    # Încarcă evenimentele existente la pornire
    incarca_evenimente(evenimente, filename)
    
    while True:
        print("=== SISTEM GESTIONARE EVENIMENTE ===")
        print("1. Adaugă eveniment")
        print("2. Afișează toate evenimentele")
        print("3. Caută eveniment după nume")
        print("4. Evenimente viitoare")
        print("5. Total încasări")
        print("6. Ieșire")
        
        optiune = input("Alege o opțiune: ")
        
        if optiune == "1":
            adauga_eveniment(evenimente, filename)
        elif optiune == "2":
            afiseaza_evenimente(evenimente)
        elif optiune == "3":
            cauta_eveniment(evenimente)
        elif optiune == "4":
            evenimente_viitoare(evenimente)
        elif optiune == "5":
            total_incasari(evenimente)
        elif optiune == "6":
            salveaza_evenimente(evenimente, filename)  # Salvează înainte de ieșire
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă. Încearcă din nou!\n")

if __name__ == "__main__":
    main()