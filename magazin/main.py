from produs import Produs
import os 

def scrie_in_fisier(produs):
    with open("magazin.txt", "a") as f:
        f.write(str(produs) + "\n")

def citeste_din_fisier():
    if not os.path.exists("magazin.txt"):
        with open("magazin.txt", "w") as f:
            pass

    with open("magazin.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

produs1 = Produs("Laptop" , "Electronice" , 3000 ,10)
produs2 = Produs("Mouse" , "Electronice" , 150 , 50)
produs3 = Produs("Telefon" , "Electronice" , 2000 , 20)

scrie_in_fisier(produs1)
scrie_in_fisier(produs2)
scrie_in_fisier(produs3)

produse = citeste_din_fisier()
for p in produse:
    print(p)
