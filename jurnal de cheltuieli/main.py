from cheltuiala import Cheltuiala
import os 

def incarca_cheltuieli(nume_fisier):
    cheltuieli = []
    if os.path.exists(nume_fisier):
        with open(nume_fisier, "r") as f:
            for line in f:
                descriere, suma, data, categorie = line.strip().split(",")
                cheltuiala = Cheltuiala(descriere, float(suma), data, categorie)
                cheltuieli.append(cheltuiala)
    return cheltuieli

def salveaza_cheltuieli(nume_fisier, cheltuieli):
    with open(nume_fisier, "w") as f:
        for cheltuiala in cheltuieli:
            f.write(f"{cheltuiala.descriere}, {cheltuiala.suma}, {cheltuiala.data}, {cheltuiala.categorie} \n")

def adauga_cheltuiala(cheltuieli, cheltuiala):
    cheltuieli.append(cheltuiala)
    salveaza_cheltuieli("cheltuieli.txt", cheltuieli)

def afiseaza_cheltuieli(cheltuieli):
    for cheltuiala in cheltuieli:
        print(cheltuiala)

def sterge_cheltuiala(cheltuieli, cheltuiala):
    if cheltuiala in cheltuieli:
        cheltuieli.remove(cheltuiala)
        salveaza_cheltuieli("cheltuieli.txt", cheltuieli)

storage_file = "cheltuieli.txt"
cheltuieli = incarca_cheltuieli(storage_file)

while True:
    print("1. Adauga Cheltuiala")
    print("2. Afiseaza Cheltuieli")
    print("3. Sterge Cheltuiala")
    print("4. Iesire")
    optiune = input("Alege o optiune: ")

    if optiune == "1":
        descriere = input("Introdu descrierea cheltuielii: ")
        suma = float(input("Introdu suma cheltuielii: "))
        data = input("Introdu data cheltuielii: ")
        categorie = input("Introdu categoria cheltuielii: ")
        cheltuiala = Cheltuiala(descriere, suma, data, categorie)
        adauga_cheltuiala(cheltuieli, cheltuiala)
    elif optiune == "2":
        afiseaza_cheltuieli(cheltuieli)
    elif optiune == "3":
        descriere = input("Introdu descrierea cheltuielii de sters: ")
        suma = float(input("Introdu suma cheltuielii de sters: "))
        data = input("Introdu data cheltuielii de sters: ")
        categorie = input("Introdu categoria cheltuielii de sters: ")
        cheltuiala = Cheltuiala(descriere, suma, data, categorie)
        sterge_cheltuiala(cheltuieli, cheltuiala)
    elif optiune == "4":
        break
    else:
        print("Optiune invalida. Incearca din nou.")