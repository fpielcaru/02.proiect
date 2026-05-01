from masina import Masina
import os

def scrie_in_fisier(masina):
    with open("masini.txt", "a") as f:
        f.write(str(masina) + "\n")

def citeste_din_fisier():
    if not os.path.exists("masini.txt"):
        with open("masini.txt", "x") as f:
            pass
    with open("masini.txt", "r") as f:
        return [line.strip() for line in f.readlines()]
    
masina1 = Masina("Toyota", "Supra MK4", 1998, 400)
masina2 = Masina("Nissan", "Skyline R34", 1998, 350)

scrie_in_fisier(masina1)
scrie_in_fisier(masina2)

masini = citeste_din_fisier()
for masina in masini:
    print(masina)