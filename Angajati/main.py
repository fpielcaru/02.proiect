from angajat import Angajat
import os

def scrie_in_fisier(angajati, nume_fisier):
    with open(nume_fisier, "w") as f:
        for angajat in angajati:
            f.write(str(angajat) + "\n")

def citeste_din_fisier(nume_fisier):
    angajati = []
    with open(nume_fisier, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                angajati.append(Angajat(*line.split(", ")))
    return angajati

a1 = Angajat("Ion Popescu", "Programator", 5000, 2)
a2 = Angajat("Maria Staicu", "Designer", 4500, 3)
a3 = Angajat("Ionela Ionescu", "Manager Marketing", 6000, 2)

angajati = [a1, a2, a3]

nume_fisier = "angajati.txt"

scrie_in_fisier(angajati, nume_fisier)
angajati_cititi = citeste_din_fisier(nume_fisier)
for a in angajati_cititi:
    print(a)

